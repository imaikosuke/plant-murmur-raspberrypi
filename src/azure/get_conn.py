import os
from dotenv import load_dotenv

load_dotenv()

# AzureのPostgreSQLサーバーに接続するためのURIを取得する関数
def get_connection_uri():
    dbhost = os.getenv("AZURE_POSTGRESQL_HOST")
    dbname = os.getenv("AZURE_POSTGRESQL_DATABASE")
    dbuser = os.getenv("AZURE_POSTGRESQL_USER")
    password = os.getenv("AZURE_POSTGRESQL_PASSWORD")
    sslmode = "require"
    db_uri = f"postgresql://{dbuser}:{password}@{dbhost}/{dbname}?sslmode={sslmode}"
    return db_uri
