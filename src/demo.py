import os
# from datetime import datetime
from azure_storage import AzureBlobStorage
from azure_sql import AzureSQLDatabase
from dotenv import load_dotenv

load_dotenv()
# Azure Blob Storage and SQL Database connection strings
AZURE_BLOB_CONNECTION_STRING = os.getenv("AZURE_BLOB_CONNECTION_STRING")
AZURE_BLOB_CONTAINER_NAME = "photos"
AZURE_SQL_CONNECTION_STRING = os.getenv("AZURE_SQL_CONNECTION_STRING")

def upload_demo_data():
    # デモデータの準備
    demo_soil_moisture = 30  # 任意の土壌水分値
    demo_photo_path = "demo_photo.jpg"  # 任意の写真パス

    # デモ用の写真ファイルを作成
    with open(demo_photo_path, "wb") as f:
        f.write(os.urandom(1024))  # 1KBのランダムデータを書き込み

    # Azure Blob Storageに写真をアップロード
    azure_blob_storage = AzureBlobStorage(AZURE_BLOB_CONNECTION_STRING, AZURE_BLOB_CONTAINER_NAME)
    photo_url = azure_blob_storage.upload_file(demo_photo_path)
    print(photo_url)

    # Azure SQL Databaseにデータを挿入
    azure_sql_db = AzureSQLDatabase(AZURE_SQL_CONNECTION_STRING)
    azure_sql_db.insert_condition(demo_soil_moisture)
    if photo_url:
        azure_sql_db.insert_photo(photo_url)

    # デモ用の写真ファイルを削除
    os.remove(demo_photo_path)

if __name__ == "__main__":
    upload_demo_data()
