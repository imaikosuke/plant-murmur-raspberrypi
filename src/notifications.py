import requests
import random

# 閾値を超えたらLINEに通知を送る
def send_line_notification(token, threshold, value):
    water_messages = ["喉乾いたぁ", "水ほしいな", "もうカラカラだよ～", "水ちょーだい！", "水！", "水やりまだ～？"]
    try:
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": "Bearer " + token}
        message = water_messages[random.randint(0, 5)]

        if value < threshold:
            payload = {"message": message}
            response = requests.post(url, headers=headers, params=payload)
            if response.status_code != 200:
                print("Error sending LINE notification:", response.text)
    except OSError:
        pass
