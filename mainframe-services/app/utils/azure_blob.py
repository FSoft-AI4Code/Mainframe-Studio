from azure.storage.blob import BlobServiceClient
from app.config.settings import settings


class AzureBlobStorage:
    def __init__(self):
        self.connection_string = settings.AZURE_STORAGE_CONNECTION_STRING
        self.container_name = settings.AZURE_STORAGE_CONTAINER_NAME
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

    async def download_blob(self, blob_name: str) -> bytes:
        """Download a file from Azure Blob Storage"""
        try:
            container_client = self.blob_service_client.get_container_client(self.container_name)
            blob_client = container_client.get_blob_client(blob_name)

            download_stream = blob_client.download_blob()
            return download_stream.readall()
        except Exception as e:
            raise Exception(f"Error downloading blob: {str(e)}")

    async def read_blob(self, blob_path: str) -> str:
        """Asynchronously read a text blob from Azure Blob Storage"""
        try:
            content_bytes = await self.download_blob(blob_path)
            return content_bytes.decode("utf-8")
        except Exception as e:
            raise Exception(f"Error reading blob: {str(e)}")
