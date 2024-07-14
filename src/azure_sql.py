from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime
from sqlalchemy.sql import insert
from datetime import datetime

# Azure SQL Database　へのデータ追加を行うクラス
class AzureSQLDatabase:
    def __init__(self, server, database, username, password):
        driver = '{ODBC Driver 17 for SQL Server}'
        connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
        self.engine = create_engine(connection_string)
        self.metadata = MetaData(self.engine)
        self.conditions = Table('conditions', self.metadata,
                                Column('id', Integer, primary_key=True, autoincrement=True),
                                Column('moisture', Integer),
                                Column('timestamp', DateTime))
        self.photos = Table('photos', self.metadata,
                            Column('photo_id', Integer, primary_key=True, autoincrement=True),
                            Column('photo_url', String),
                            Column('timestamp', DateTime))

    # 土壌湿度を追加するメソッド
    def insert_condition(self, moisture):
        timestamp = datetime.now()
        query = insert(self.conditions).values(moisture=moisture, timestamp=timestamp)
        with self.engine.connect() as connection:
            connection.execute(query)
        print(f"Inserted condition: moisture={moisture}, timestamp={timestamp}")

    # 写真を追加するメソッド
    def insert_photo(self, photo_url):
        timestamp = datetime.now()
        query = insert(self.photos).values(photo_url=photo_url, timestamp=timestamp)
        with self.engine.connect() as connection:
            connection.execute(query)
        print(f"Inserted photo: photo_url={photo_url}, timestamp={timestamp}")
