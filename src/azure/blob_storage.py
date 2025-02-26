from azure.storage.blob import BlobServiceClient
import os

# Azure Blob Storageにファイルをアップロードするクラス
class AzureBlobStorage:
    def __init__(self, connection_string, container_name):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)

    # 写真ファイルをAzure Blob Storageにアップロードするメソッド
    def upload_file(self, file_path):
        try:
            file_name = os.path.basename(file_path)
            blob_client = self.container_client.get_blob_client(file_name)

            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)

            blob_url = blob_client.url
            print(f"Uploaded to Azure Blob Storage: {blob_url}")
            return blob_url
        except Exception as e:
            print(f"Error uploading to Azure Blob Storage: {e}")
            return None
