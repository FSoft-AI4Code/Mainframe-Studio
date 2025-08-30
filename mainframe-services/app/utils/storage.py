import os
from fastapi import UploadFile
from app.config.settings import settings


async def save_upload_file(upload_file: UploadFile, destination: str):
    try:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        with open(destination, "wb") as buffer:
            content = await upload_file.read()
            buffer.write(content)
        return True
    except Exception as e:
        print(f"Error saving file: {str(e)}")
        return False


def delete_file(file_path: str):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    except Exception as e:
        print(f"Error deleting file: {str(e)}")
        return False
