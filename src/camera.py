import subprocess
import datetime

# 現在の日時をファイル名にした写真を指定したディレクトリに保存
def capture_photo(photo_directory):
    now = datetime.datetime.today()
    
    # 例：20240712131108.jpg
    filename = "{0}{1:02d}{2:02d}{3:02d}{4:02d}{5:02d}.jpg".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    filepath = f"{photo_directory}/{filename}"
    args = ['/usr/bin/fswebcam', filepath]
    
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error capturing photo:", result.stderr)
    else:
        print("Photo captured:", filepath)
