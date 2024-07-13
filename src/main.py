import os
from dotenv import load_dotenv
from time import sleep
import notifications
import camera
from soil_moisture import SoilMoistureSensor

load_dotenv()
LINE_TOKEN = os.getenv("LINE_TOKEN")
THRESHOLD = 20.0  # 土壌水分の閾値（パーセント）
PHOTO_DIRECTORY = "/hoge/fuga/piyo"

def main():
    sensor = SoilMoistureSensor()
    try:
        while True:
            soil_moisture_percentage = sensor.get_soil_moisture()
            print(f"Soil Moisture Percentage: {soil_moisture_percentage:.1f}%")
            notifications.send_line_notification(LINE_TOKEN, THRESHOLD, soil_moisture_percentage)
            camera.capture_photo(PHOTO_DIRECTORY)
            sleep(1800)  # 30分ごとに実行
    except KeyboardInterrupt:
        print("Program terminated.")
    finally:
        sensor.close()

if __name__ == "__main__":
    main()
