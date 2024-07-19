import os
from dotenv import load_dotenv
from time import sleep
import notifications
import camera
from soil_moisture import SoilMoistureSensor
from azure_storage import AzureBlobStorage
from azure_sql import PostgreSQLDatabase
from brightness import BrightnessSensor

load_dotenv()
LINE_TOKEN = os.getenv("LINE_TOKEN")
AZURE_BLOB_CONNECTION_STRING = os.getenv("AZURE_BLOB_CONNECTION_STRING")
PHOTO_DIRECTORY = "/home/Pi/photos"
AZURE_BLOB_CONTAINER_NAME = "photos"
SOIL_MOISTURE_THRESHOLD = 20.0  # 土壌水分の閾値（パーセント）
BRIGHTNESS_THRESHOLD = 500  # 明るさの閾値

def main():
    sensor = SoilMoistureSensor()
    brightness_sensor = BrightnessSensor(clockpin=11, mosipin=10, misopin=9, cspin=8)
    azure_blob_storage = AzureBlobStorage(AZURE_BLOB_CONNECTION_STRING, AZURE_BLOB_CONTAINER_NAME)
    postgresql_db = PostgreSQLDatabase()

    try:
        while True:
            soil_moisture_percentage = sensor.get_soil_moisture()
            print(f"Soil Moisture Percentage: {soil_moisture_percentage:.1f}%")

            # 土壌水分データをPostgreSQLに挿入
            postgresql_db.insert_condition(int(soil_moisture_percentage))

            # 土壌水分が閾値以下の場合、LINE通知を送信
            notifications.send_line_notification(LINE_TOKEN, SOIL_MOISTURE_THRESHOLD, soil_moisture_percentage)

            # 明るさを取得
            brightness = brightness_sensor.get_brightness()
            print(f"Brightness: {brightness}")

            # 明るさが閾値以下の場合、LINE通知を送信
            if brightness < BRIGHTNESS_THRESHOLD:
                notifications.send_line_notification(LINE_TOKEN, BRIGHTNESS_THRESHOLD, brightness)

            # 写真を撮影し、Azure Blob Storageにアップロード
            photo_path = camera.capture_photo(PHOTO_DIRECTORY)
            if photo_path:
                photo_url = azure_blob_storage.upload_file(photo_path)
                if photo_url:
                    # 写真情報をPostgreSQLに挿入
                    postgresql_db.insert_photo(photo_url)

            sleep(1800)  # 30分ごとに実行
    except KeyboardInterrupt:
        print("Program terminated.")
    finally:
        sensor.close()
        brightness_sensor.close()

if __name__ == "__main__":
    main()
