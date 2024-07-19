import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection_uri():

    # Read URI parameters from the environment
    dbhost = os.getenv("AZURE_POSTGRESQL_HOST")
    dbname = os.getenv("AZURE_POSTGRESQL_DATABASE")
    dbuser = os.getenv("AZURE_POSTGRESQL_USER")
    password = os.getenv("AZURE_POSTGRESQL_PASSWORD")
    sslmode = "require"

    # Construct connection URI
    db_uri = f"postgresql://{dbuser}:{password}@{dbhost}/{dbname}?sslmode={sslmode}"
    return db_uri
