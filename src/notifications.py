import requests
import os
from dotenv import load_dotenv
import random

load_dotenv()

LINE_API_URL = os.getenv("LINE_API_URL")

def send_line_water_notification():
    water_messages = ["喉乾いたぁ", "水ほしいな", "もうカラカラだよ～", "水ちょーだい！", "水！", "水やりまだ～？"]
    message = water_messages[random.randint(0, 5)]
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {"message": message}
    response = requests.post(LINE_API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Error sending notification: {response.status_code}, {response.text}")

def send_line_brightness_notification(token):
    brightness_messages = ["暗いよ～", "もう少し明るくして～", "明るくして～", "もう暗いよ", "もう薄暗いよ～", "真っ暗でこわいぃ"]
    message = brightness_messages[random.randint(0, 5)]
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {"message": message}
    response = requests.post(LINE_API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Error sending notification: {response.status_code}, {response.text}")
