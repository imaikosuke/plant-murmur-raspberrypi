import psycopg2
from src.azure.get_conn import get_connection_uri

# PostgreSQLに接続し、データを挿入するクラス
class PostgreSQLDatabase:
    def __init__(self):
        conn_string = get_connection_uri()
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()

    # 指定した土壌水分をconditionsテーブルに挿入するメソッド
    def insert_condition(self, moisture: int):
        try:
            self.cur.execute("INSERT INTO conditions (moisture) VALUES (%s)", (moisture,))
            self.conn.commit()
            print("Inserted condition successfully.")
        except Exception as e:
            print(f"Error inserting data: {e}")

    # 指定した写真URLをphotosテーブルに挿入するメソッド
    def insert_photo(self, photo_url: str):
        try:
            self.cur.execute("INSERT INTO photos (photo_url) VALUES (%s)", (photo_url,))
            self.conn.commit()
            print("Inserted photo successfully.")
        except Exception as e:
            print(f"Error inserting data: {e}")

    # データベース接続を閉じるメソッド
    def close(self):
        self.cur.close()
        self.conn.close()
