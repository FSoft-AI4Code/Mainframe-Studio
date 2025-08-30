from bson import ObjectId


async def get_blob_path(db, file_name, repository_id, file_type):
    pipeline = [
        {"$match": {
            "repository_id": ObjectId(repository_id),
        }},
        {"$unwind": "$result.assessment"},
        {"$match": {
            "result.assessment.name": file_name,
            "result.assessment.label": file_type
        }},
        {"$project": {
            "_id": 0,
            "path": "$result.assessment.path"
        }}
    ]
    blob_path = await db.assessments.aggregate(pipeline).to_list(1)
    if not blob_path or type(blob_path) != list:
        raise FileNotFoundError
    path = blob_path[0].get("path")
    return path