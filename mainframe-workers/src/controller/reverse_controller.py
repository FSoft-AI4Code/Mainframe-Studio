from typing import List, Dict, Any, Optional
from loguru import logger
from bson import ObjectId
from model.reverse_model import CopybookReverseModel
from database.mongodb import get_database
from schema.reverse_engineering import ReverseEngineeringStatus, ReverseEngineeringUpdate
from datetime import datetime


class ReverseController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.reverse_engineering


    def query_copy_content(self, filename: str) -> Optional[str]:
        """
        Query copybook content from reverse engineering collection
        """
        try:
            result = self.collection.find_one({"name": filename})
            if result:
                return result.get("content", "")
            return None
        except Exception as e:
            logger.error("Error querying copybook content",
                         error=str(e), filename=filename)
            return None

    def query_reverse_engineering(
        self, 
        name: str, 
        repository_id: str, 
        type_: str,
        projection: Optional[Dict[str, int]] = None,
    ) -> Optional[dict]:
        """Query output from reverse engineering collection"""
        try:
            result = self.collection.find_one(
                {
                    "name": name,
                    "repository_id": ObjectId(repository_id),
                    "type": type_,
                    "output": {"$exists": True}
                }, 
                projection
            )
                
            return result.get("output", {}) if result else None
        except Exception as e:
            logger.error(
                "Error querying reverse engineering data",
                error=str(e),
                name=name,
                repository_id=repository_id,
                type=type_,
            )
            return None

    def query_reverse_engineering_full(
        self,
        name: str,
        repository_id: str,
        type_: str,
        projection: Optional[Dict[str, int]] = None,
    ) -> Optional[dict]:
        """Query reverse engineering collection returning full document"""
        try:
            result = self.collection.find_one(
                {
                    "name": name,
                    "repository_id": ObjectId(repository_id),
                    "type": type_,
                },
                projection,
            )

            return result
        except Exception as e:
            logger.error(
                "Error querying reverse engineering data",
                error=str(e),
                name=name,
                repository_id=repository_id,
                type=type_,
            )
            return None
        
    def query_output_content(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        Query copybook output from reverse engineering collection
        """
        try:
            result = self.collection.find_one({"name": filename})
            if result:
                return result.get("output", {})
            return None
        except Exception as e:
            logger.error("Error querying copybook output",
                         error=str(e), filename=filename)
            return None

    def save_copybook_reverse(self, repository_id: str, type_: str, parsed_copybooks: List[Dict[str, Any]]) -> Dict[str, Any]:
        # Track successful and failed operations
        updated_count = 0
        inserted_count = 0
        failed_count = 0
        failed_copybooks = []
        operation_results = []

        for copybook in parsed_copybooks:
            try:
                model = CopybookReverseModel(
                    name=copybook.get('name', ''),
                    content=copybook.get('content', ''),
                    output=copybook.get('output', {}),
                    path=copybook.get('path', ''),
                    url=copybook.get('url', ''),
                    status=copybook.get('status', ''),
                )

                # Prepare update operation
                result = self.collection.update_one(
                    filter={
                        'name': model.name, 
                        'repository_id': ObjectId(repository_id),
                        'type': type_
                    },  # Match by name
                    update={
                        '$set': model.model_dump()
                    },
                    upsert=True
                )

                if result.matched_count > 0:
                    updated_count += 1
                elif result.upserted_id:
                    inserted_count += 1

                operation_results.append({
                    'name': model.name,
                    'operation': 'update' if result.matched_count > 0 else 'insert',
                    'id': str(result.upserted_id) if result.upserted_id else None
                })
            except Exception as e:
                failed_count += 1
                failed_copybooks.append({
                    'name': copybook.get('name', ''),
                    'error': str(e)
                })
                logger.error(f"Failed to save copybook {copybook.get('name', '')}: {str(e)}")

        return {
            "status": "success" if failed_count == 0 else "partial",
            "message": f"Processed {len(parsed_copybooks)} copybooks: {updated_count} updated, {inserted_count} inserted, {failed_count} failed",
            "failed_count": failed_count,
            "failed_copybooks": failed_copybooks if failed_count > 0 else None
        }

    def save_reverse_engineering(self, name: str, repository_id: str, reverse_program: ReverseEngineeringUpdate, type: str) -> Dict[str, Any]:
        """
        Save COBOL reverse engineering result to database using upsert operation

        Args:
            name (str): The name of the program
            repository_id (str): The repository ID
            reverse_program (ReverseEngineeringUpdate): The reverse engineering update data

        Returns:
            Dict[str, Any]: Result of the save operation containing status and message
        """
        try:
            result = self.collection.update_one(
                filter={
                    'name': name,
                    'repository_id': ObjectId(repository_id),
                    'type': type
                },
                update={
                    '$set': {**reverse_program.model_dump(exclude_none=True)}
                },
                upsert=True
            )

            if result.matched_count > 0:
                return {
                    "status": "success",
                    "message": "Successfully updated reverse engineering result"
                }
            elif result.upserted_id:
                return {
                    "status": "success",
                    "message": "Successfully inserted reverse engineering result",
                }
            else:
                return {
                    "status": "error",
                    "message": "Failed to save reverse engineering result"
                }

        except Exception as e:
            logger.error(
                "Error saving COBOL reverse engineering result", error=str(e))
            return {
                "status": "error",
                "message": f"Error saving reverse engineering result: {str(e)}"
            }

    def map_screen_access(self, screen_name: str, program_name: str, repository_id: str) -> Dict[str, Any]:
        """
        Map program to screen access. If screen doesn't exist, create new one.
        If screen exists, append program to programs list if not already present.
        A program can only be mapped to one screen.

        Args:
            screen_name (str): Name of the screen
            program_name (str): Name of the program to be mapped
            repository_id (str): ID of the repository

        Returns:
            Dict[str, Any]: Result of the operation containing status and message
        """
        try:
            # First, check if program exists in any screen
            existing_mapping = self.db.screen_access.find_one({
                "repository_id": ObjectId(repository_id),
                "programs": {"$in": [program_name]}
            })

            if existing_mapping and existing_mapping["screen"] != screen_name:
                return {
                    "status": "success",
                    "message": f"Program {program_name} is already mapped to screen {existing_mapping['screen']}"
                }

            # Try to update existing screen by adding program to programs array
            result = self.db.screen_access.update_one(
                {
                    "screen": screen_name,
                    "repository_id": ObjectId(repository_id)
                },
                {
                    "$addToSet": {  # $addToSet ensures no duplicates
                        "programs": program_name
                    }
                }
            )

            # If no screen was found (matched_count = 0), insert new one
            if result.matched_count == 0:
                result = self.db.screen_access.insert_one({
                    "screen": screen_name,
                    "programs": [program_name],
                    "repository_id": ObjectId(repository_id)
                })
                return {
                    "status": "success",
                    "message": f"Created new screen access mapping for {screen_name}",
                    "inserted_id": str(result.inserted_id)
                }

            # If screen exists but program was not in array (modified_count > 0)
            if result.modified_count > 0:
                return {
                    "status": "success",
                    "message": f"Added program {program_name} to screen {screen_name}"
                }

            # If screen exists but program was already in array (modified_count = 0)
            return {
                "status": "success",
                "message": f"Program {program_name} already mapped to screen {screen_name}"
            }

        except Exception as e:
            logger.error("Error mapping screen access",
                        error=str(e),
                        screen=screen_name,
                        program=program_name,
                        repository_id=repository_id)
            return {
                "status": "error",
                "message": f"Error mapping screen access: {str(e)}"
            }

    def save_program_summary(self, name: str, repository_id: str, summary: Dict[str, Any], type_: str) -> Dict[str, Any]:
        """
        Save program summary to the reverse engineering collection and update execution flow nodes
        with their corresponding paragraph logic.
        
        Args:
            name (str): Program name
            repository_id (str): Repository ID
            summary (Dict[str, Any]): Program summary data
            type_ (str): Program type (e.g., 'COBOL')
            
        Returns:
            Dict[str, Any]: Result of the save operation
        """
        try:
            # First get the existing execution flow graph
            result = self.collection.find_one({
                'name': name,
                'repository_id': ObjectId(repository_id),
                'type': type_
            }, {'output.exec_flow': 1})

            if not result or 'output' not in result or 'exec_flow' not in result['output']:
                return {
                    "status": "error",
                    "message": "Execution flow not found for program"
                }

            exec_flow = result['output']['exec_flow']
            nodes = exec_flow.get('nodes', [])
            
            # Update nodes with their corresponding paragraph logic
            updated_nodes = []
            for node in nodes:
                node_data = node.copy()
                if node['name'] in summary:
                    node_data['paragraph_logic'] = summary[node['name']]["paragraph_logic"]
                updated_nodes.append(node_data)

            # Update both the summary and exec_flow with updated nodes
            result = self.collection.update_one(
                filter={
                    'name': name,
                    'repository_id': ObjectId(repository_id),
                    'type': type_
                },
                update={
                    '$set': {
                        'output.processing_logic.paragraph_level': summary,
                        'output.exec_flow.nodes': updated_nodes,
                        'updated_at': datetime.utcnow()
                    }
                }
            )
            
            if result.matched_count > 0:
                return {
                    "status": "success",
                    "message": f"Successfully updated summary for program {name}"
                }
            else:
                return {
                    "status": "error", 
                    "message": f"Program {name} not found"
                }

        except Exception as e:
            logger.error(f"Error saving program summary: {str(e)}", 
                        program=name, 
                        repository_id=repository_id)
            return {
                "status": "error",
                "message": f"Error saving program summary: {str(e)}"
            }

    def save_statement_summary(self, name: str, repository_id: str, summary: Dict[str, Any], type_: str) -> Dict[str, Any]:
        """
        Save statement level summary to the reverse engineering collection under output.summary.statement_level
        
        Args:
            name (str): Program name
            repository_id (str): Repository ID
            summary (Dict[str, Any]): Statement summary data
            type_ (str): Program type (e.g., 'COBOL')
            
        Returns:
            Dict[str, Any]: Result of the save operation
        """
        try:
            result = self.collection.update_one(
                filter={
                    'name': name,
                    'repository_id': ObjectId(repository_id),
                    'type': type_
                },
                update={
                    '$set': {
                        'output.processing_logic.statement_level': summary,
                        'updated_at': datetime.utcnow()
                    }
                }
            )
            
            if result.matched_count > 0:
                return {
                    "status": "success",
                    "message": f"Successfully updated statement summary for program {name}"
                }
            else:
                return {
                    "status": "error", 
                    "message": f"Program {name} not found"
                }

        except Exception as e:
            logger.error(f"Error saving statement summary: {str(e)}", 
                        program=name, 
                        repository_id=repository_id)
            return {
                "status": "error",
                "message": f"Error saving statement summary: {str(e)}"
            }
