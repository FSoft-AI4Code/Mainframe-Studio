from fastapi import APIRouter, Depends, HTTPException, Query, Path
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.database import get_database
from app.controllers import utility_controller
from app.schemas.common_schema import ResponseBase, PaginationParams
from app.schemas.utility_schema import (
    UtilityCreate,
    UtilityUpdate,
    UtilityResponse,
    UtilityListResponse
)
from app.security import auth
import pandas as pd
from io import BytesIO
from fastapi.responses import StreamingResponse
from datetime import datetime
import openpyxl
from bson import ObjectId
from typing import Optional

router = APIRouter()

@router.post(
    "/repositories/{repository_id}/process-utilities",
    summary="Process Repository Utilities",
    description="""
    Process nodes with label 'UTILITY' from a repository and create utilities.
    
    This endpoint:
    1. Finds all nodes with label 'UTILITY' in the repository
    2. Creates utility records for each node if they don't already exist
    3. Automatically categorizes utilities based on their names
    4. Populates descriptions from IBM_MAINFRAME_UTILITIES mapping
    
    Returns:
    - Number of utilities created
    - Success message
    
    Raises:
    - 500: For any server errors
    """,
    response_model=ResponseBase[dict]
)
async def process_repository_utilities(
    repository_id: str = Path(..., description="The ID of the repository to process utilities from"),
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    """Process nodes with label 'UTILITY' from a repository and create utilities"""
    try:
        # Validate repository_id format
        try:
            ObjectId(repository_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid repository_id format. Must be a valid MongoDB ObjectId."
            )

        created_count = await utility_controller.process_nodes_to_utilities(db, repository_id)
        return ResponseBase(data={
            "message": f"Successfully processed {created_count} utilities",
            "created_count": created_count
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/repositories/{repository_id}/",
    summary="Create Utility",
    description="""
    Create a new utility record.
    
    Required fields:
    - name: Name of the utility
    - category: Category of the utility
    - node_id: ID of the associated node
    - repository_id: ID of the repository
    
    Optional fields:
    - description: Description of the utility (will be populated from IBM_MAINFRAME_UTILITIES if available)
    
    Returns:
    - Created utility object
    
    Raises:
    - 500: For any server errors
    """,
    response_model=ResponseBase[UtilityResponse]
)
async def create_utility(
    db: AsyncIOMotorClient = Depends(get_database),
    repository_id: str = Path(..., description="The ID of the repository to get categories for"),
    file_name: str = Query(..., description="The name of the utility file"),
    label: str = Query(..., description="The label of the utility to create"),
    category_name: str = Query(..., description="The name of the category for the utility"),
    comment: Optional[str] = Query(None, description="Optional comment for the utility"),
    description = Query(None, description="Optional description for the utility"),
    current_user: auth.User = Depends(auth.get_current_user),
):
    """Create a new utility"""
    try:
        created_utility = await utility_controller.create_utility(db, repository_id, file_name, label, category_name, comment, description)
        return ResponseBase(data=created_utility)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/repositories/{repository_id}/category",
            summary="Get Repository Categories",
            description="""
            """)
async def get_repository_categories(
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user),
    repository_id: str = Path(..., description="The ID of the repository to get categories for")
):
    """Get all utility categories for a repository"""
    try:
        utility_category = await utility_controller.get_category_by_project(db, repository_id)
        return ResponseBase(data=utility_category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/{utility_id}",
    summary="Get Utility by ID",
    description="""
    Retrieve a specific utility by its ID.
    
    Args:
    - utility_id: The ID of the utility to retrieve
    
    Returns:
    - Utility object with all its details
    
    Raises:
    - 404: If utility is not found
    - 400: If utility_id format is invalid
    - 500: For any server errors
    """,
    response_model=ResponseBase[UtilityResponse]
)
async def get_utility(
    utility_id: str = Path(..., description="The ID of the utility to retrieve"),
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    """Get a utility by ID"""
    try:
        # Validate utility_id format
        try:
            ObjectId(utility_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid utility_id format. Must be a valid MongoDB ObjectId."
            )

        utility = await utility_controller.get_utility(db, utility_id)
        if not utility:
            raise HTTPException(status_code=404, detail="Utility not found")
        return ResponseBase(data=utility)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/repositories/{repository_id}",
    summary="Get Repository Utilities",
    description="""
    Get all utilities for a repository with pagination.
    
    Args:
    - repository_id: The ID of the repository
    - skip: Number of records to skip (for pagination)
    - limit: Maximum number of records to return (for pagination)
    
    Returns:
    - List of utilities
    - Total count of utilities
    - Pagination information (skip, limit)
    
    Raises:
    - 400: If repository_id format is invalid
    - 500: For any server errors
    """,
    response_model=ResponseBase[UtilityListResponse]
)
async def get_repository_utilities(
    repository_id: str = Path(..., description="The ID of the repository to get utilities from"),
    pagination: PaginationParams = Depends(),
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    """Get all utilities for a repository with pagination"""
    try:
        # Validate repository_id format
        try:
            ObjectId(repository_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid repository_id format. Must be a valid MongoDB ObjectId."
            )

        utilities, total = await utility_controller.get_utilities(
            db,
            repository_id,
            skip=pagination.skip,
            limit=pagination.limit
        )
        return ResponseBase(data={
            "utilities": utilities,
            "total": total,
            "skip": pagination.skip,
            "limit": pagination.limit
        })
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put(
    "/{utility_id}",
    summary="Update Utility",
    description="""
    Update an existing utility.
    
    Args:
    - utility_id: The ID of the utility to update
    
    Optional fields that can be updated:
    - description: New description
    - category: New category
    
    Note: The utility name cannot be updated as it is a fixed identifier.
    
    Returns:
    - Updated utility object
    
    Raises:
    - 404: If utility is not found
    - 400: If utility_id format is invalid
    - 500: For any server errors
    """,
    response_model=ResponseBase[UtilityResponse]
)
async def update_utility(
    utility_id: str = Path(..., description="The ID of the utility to update"),
    utility: UtilityUpdate = None,
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    """Update a utility"""
    try:
        # Validate utility_id format
        try:
            ObjectId(utility_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid utility_id format. Must be a valid MongoDB ObjectId."
            )

        # Get the existing utility to ensure it exists
        existing_utility = await utility_controller.get_utility(db, utility_id)
        if not existing_utility:
            raise HTTPException(status_code=404, detail="Utility not found")

        # Update the utility
        updated_utility = await utility_controller.update_utility(db, utility_id, utility)
        return ResponseBase(data=updated_utility)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(
    "/{utility_id}",
    summary="Delete Utility",
    description="""
    Delete a utility by its ID.
    
    Args:
    - utility_id: The ID of the utility to delete
    
    Returns:
    - Success message
    
    Raises:
    - 404: If utility is not found
    - 400: If utility_id format is invalid
    - 500: For any server errors
    """,
    response_model=ResponseBase[dict]
)
async def delete_utility(
    utility_id: str = Path(..., description="The ID of the utility to delete"),
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    """Delete a utility"""
    try:
        # Validate utility_id format
        try:
            ObjectId(utility_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid utility_id format. Must be a valid MongoDB ObjectId."
            )

        success = await utility_controller.delete_utility(db, utility_id)
        if not success:
            raise HTTPException(status_code=404, detail="Utility not found")
        return ResponseBase(data={"message": "Utility successfully deleted"})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/repositories/{repository_id}/excel",
    summary="Generate Excel Report",
    description="""
    Generate an Excel report containing all utilities for a specific repository.
    
    The report includes the following information for each utility:
    - Name
    - Description (automatically populated from IBM_MAINFRAME_UTILITIES if available)
    - Category
    - Comment (user-provided notes about the utility)
    
    The Excel file is formatted with:
    - Bold headers with background color
    - Properly sized columns based on content
    - Borders for better readability
    
    Returns:
    - Excel file (.xlsx) as a downloadable attachment
    - Filename includes timestamp for uniqueness
    
    Raises:
    - 404: If no utilities are found for the repository
    - 500: For any other server errors
    """,
    response_description="Excel file containing utilities report"
)
async def generate_utilities_excel_report(
    repository_id: str = Path(..., description="The ID of the repository to generate the report for"),
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    """
    Generate an Excel report of utilities for a given repository.
    
    Args:
        repository_id (str): The ID of the repository to generate the report for
        db (AsyncIOMotorClient): MongoDB database connection
        current_user (auth.User): Currently authenticated user
        
    Returns:
        StreamingResponse: Excel file as a downloadable attachment
        
    Raises:
        HTTPException: If repository_id is invalid or no utilities are found
    """
    try:
        # Validate repository_id format
        try:
            ObjectId(repository_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid repository_id format. Must be a valid MongoDB ObjectId."
            )

        # Get all utilities for the repository without pagination
        query = {"repository_id": repository_id}
        utilities = await db.utilities.find(query).to_list(length=None)
        
        if not utilities:
            raise HTTPException(
                status_code=404,
                detail=f"No utilities found for repository {repository_id}"
            )

        # Convert to DataFrame
        data = []
        for utility in utilities:
            # Validate required fields
            if not all(key in utility for key in ["name", "category"]):
                raise HTTPException(
                    status_code=500,
                    detail="Invalid utility data: missing required fields"
                )
            
            data.append({
                "Name": utility["name"],
                "Description": utility.get("description", ""),  # Use empty string if description is None
                "Category": utility["category"],
                "Comment": utility.get("comment", "")  # Use empty string if comment is None
            })
        
        df = pd.DataFrame(data)

        # Create Excel file in memory
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Utilities', index=False)
            
            # Get workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets['Utilities']
            
            # Add some formatting
            for cell in worksheet[1]:
                cell.font = cell.font.copy(bold=True)
                cell.fill = openpyxl.styles.PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
                cell.border = openpyxl.styles.Border(
                    left=openpyxl.styles.Side(style='thin'),
                    right=openpyxl.styles.Side(style='thin'),
                    top=openpyxl.styles.Side(style='thin'),
                    bottom=openpyxl.styles.Side(style='thin')
                )
            
            # Set column widths
            for column in worksheet.columns:
                max_length = 0
                column = [cell for cell in column]
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = (max_length + 2)
                worksheet.column_dimensions[column[0].column_letter].width = adjusted_width

        # Set the pointer to the beginning of the BytesIO object
        output.seek(0)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"utilities_report_{timestamp}.xlsx"

        # Return the Excel file as a streaming response
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating Excel report: {str(e)}"
        ) 