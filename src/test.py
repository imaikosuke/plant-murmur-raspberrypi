from azure_sql import PostgreSQLDatabase

def test_postgresql_database():
    # データベース接続のインスタンスを作成
    db = PostgreSQLDatabase()
    
    # データを挿入
    db.insert_condition(45)  # Moisture value

    # データを取得して確認
    db.cur.execute("SELECT * FROM conditions")
    conditions = db.cur.fetchall()
    print("Conditions:")
    for condition in conditions:
        print(condition)

    # データベース接続を閉じる
    db.close()

if __name__ == "__main__":
    test_postgresql_database()
