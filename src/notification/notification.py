import requests
import os
from dotenv import load_dotenv
import random

load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_ID = os.getenv("LINE_CHANNEL_ID")

# 水やり通知を送信する関数
def send_line_water_notification():
    water_messages = ["喉乾いたぁ", "水ほしいな", "もうカラカラだよ～", "水ちょーだい！", "水！", "水やりまだ～？"]
    message = water_messages[random.randint(0, 5)]
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }
    push_message = {
        "to": LINE_CHANNEL_ID,
        "messages": [{"type": "text", "text": message}]
    }
    response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=push_message)
    if response.status_code != 200:
        print(f"Error sending notification: {response.status_code}, {response.text}")

# 明るさ通知を送信する関数
def send_line_brightness_notification():
    brightness_messages = ["暗いよ～", "もう少し明るくして～", "明るくして～", "もう暗いよ", "もう薄暗いよ～", "真っ暗でこわいぃ"]
    message = brightness_messages[random.randint(0, 5)]
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }
    push_message = {
        "to": LINE_CHANNEL_ID,
        "messages": [{"type": "text", "text": message}]
    }
    response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=push_message)
    if response.status_code != 200:
        print(f"Error sending notification: {response.status_code}, {response.text}")
