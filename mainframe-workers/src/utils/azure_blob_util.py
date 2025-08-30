import asyncio
import io

import charset_normalizer
import pandas as pd
from azure.storage.blob import BlobServiceClient, ContentSettings
from bson import ObjectId

from classifier import RuleBasedTextClassifierBySystem, SystemType
from config.settings import settings
from .preprocess import comment_specific_lines, clean_code

connection_string = settings.AZURE_STORAGE_CONNECTION_STRING
container_name = settings.AZURE_STORAGE_CONTAINER_NAME


def read_blob_csv(blob_name: str, connection_string: str = connection_string,
                  container_name: str = container_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string)
        container_client = blob_service_client.get_container_client(
            container_name)
        blob_client = container_client.get_blob_client(blob_name)
        blob_data = blob_client.download_blob()
        read_blob_data = blob_data.readall()
        encoding = charset_normalizer.detect(read_blob_data)["encoding"]
        df = pd.read_csv(io.BytesIO(read_blob_data),
                         escapechar="\\",
                         encoding=encoding,
                         on_bad_lines="warn",
                         )
        return df
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def write_blob_csv(blob_name: str, df: pd.DataFrame, encoding="utf-8",
                   connection_string: str = connection_string,
                   container_name: str = container_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string)
        container_client = blob_service_client.get_container_client(
            container_name)

        blob_client = container_client.get_blob_client(blob_name)

        csv_string = df.to_csv(index=False, escapechar="\\",
                               doublequote=True, encoding=encoding)
        csv_bytes = csv_string.encode(encoding)

        blob_client.upload_blob(csv_bytes, overwrite=True)

        blob_metadata = blob_client.get_blob_properties().metadata
        blob_metadata.update({"encoding": encoding})
        blob_client.set_blob_metadata(metadata=blob_metadata)

        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def read_blob_file(blob_name: str, connection_string: str = connection_string,
                   container_name: str = container_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string)
        container_client = blob_service_client.get_container_client(
            container_name)
        blob_client = container_client.get_blob_client(blob_name)
        encoding = blob_client.get_blob_properties().metadata.get("encoding")
        blob_data = blob_client.download_blob()
        content = blob_data.readall()
        encoding = charset_normalizer.detect(content)["encoding"]
        return content.decode(encoding)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def write_blob(blob_name: str, content: str, connection_string: str = connection_string,
               container_name: str = container_name, content_type: str = None):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string)
        container_client = blob_service_client.get_container_client(
            container_name)
        blob_client = container_client.get_blob_client(blob_name)

        # Set content settings if content_type is provided
        content_settings = None
        if content_type:
            content_settings = ContentSettings(content_type=content_type)

        blob_client.upload_blob(content, overwrite=True, content_settings=content_settings)
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def read_blob_content(blob_data: bytes):
    file_content = charset_normalizer.from_bytes(
        blob_data,
        cp_isolation=[
            "utf-8",
            "shift_jis",
        ],
    ).best()

    if file_content is None:
        file_content = charset_normalizer.from_bytes(blob_data).best()

        if file_content is None:
            return None, None

    return str(file_content), file_content.encoding


def classify_blobs(repo_id: str, system_type: SystemType,
                   connection_string: str = connection_string,
                   container_name: str = container_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string, timeout=120, max_connections=5)
        container_client = blob_service_client.get_container_client(
            container_name)
        blobs = container_client.list_blobs(name_starts_with=repo_id)

        outputs = []

        def classify_by_system_type(content: str, encoding: str, system_type: SystemType):
            classifier = RuleBasedTextClassifierBySystem()
            return classifier.detect(code=content, encoding=encoding, system_type=system_type)

        for blob in blobs:
            if blob.name.endswith(".csv"):
                continue
            blob_client = container_client.get_blob_client(blob)
            blob_data = blob_client.download_blob().readall()
            blob_content, encoding = read_blob_content(blob_data)

            if blob_content is None or encoding is None:
                print(f"Cannot read file {blob.name} - Repo: {repo_id}")
            else:
                content = comment_specific_lines(clean_code(blob_content))
                label = classify_by_system_type(content, encoding, system_type)

                blob_name = blob.name.split("/")[-1]
                blob_name_without_extension = blob_name.split(".")[0]

                # Upload to new standardized path
                target_blob_client = container_client.get_blob_client(
                    blob=f"{repo_id}/code/{label}/{blob_name_without_extension}")
                target_blob_client.upload_blob(blob_data, overwrite=True)

                # Set encoding metadata
                blob_metadata = target_blob_client.get_blob_properties().metadata
                blob_metadata.update({"encoding": encoding})
                target_blob_client.set_blob_metadata(metadata=blob_metadata)

                outputs.append(
                    {
                        "name": blob_name_without_extension,
                        "path": blob.name,
                        "content": content,
                        "encoding": encoding,
                        "label": label,
                    }
                )
        return pd.DataFrame(outputs)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def get_file_content_from_blob_name(db, repository_id, file_name: str, file_type: str) -> str:
    try:
        blob_content = get_file_by_blob_path(db, repository_id, file_type, file_name)
        if blob_content is None:
            raise FileNotFoundError(f"Cannot read the content of {file_name}")
        return blob_content if type(blob_content) is str else blob_content[0]
    except Exception as e:
        raise e


def get_file_content_from_blob_path(blob_path: str) -> str:
    try:
        blob_content = read_blob_file(blob_path)
        if blob_content is None:
            raise FileNotFoundError(f"Cannot read the content of {blob_path}")
        return blob_content if type(blob_content) is str else blob_content[0]
    except Exception as e:
        raise e


def get_blob_path(db, file_name, repository_id, file_type):
    try:
        reverse_data = db.reverse_engineering.find(
            {"repository_id": ObjectId(repository_id),
             "type": file_type,
             "name": file_name}
        ).to_list(length=1)
        if not reverse_data:
            raise FileNotFoundError
        path = reverse_data[0].get("path")
        return path
    except Exception as e:
        raise e

def get_file_by_blob_path(db, repository_id, file_type, file_name):
    try:
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

        blob_path = db.assessments.aggregate(pipeline).to_list(1)
        if not blob_path or type(blob_path) != list:
            raise FileNotFoundError
        path = blob_path[0].get("path")
        return read_blob_file(path)
    except Exception as e:
        raise e
