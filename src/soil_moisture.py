import spidev
import time

# 土壌湿度センサーを操作するクラス
class SoilMoistureSensor:
    def __init__(self, spi_channel=0, spi_device=0, max_speed_hz=1350000):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_channel, spi_device)
        self.spi.max_speed_hz = max_speed_hz

    # チャンネル読み取りメソッド
    def read_channel(self, channel):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    # アナログ値をパーセンテージに変換するメソッド
    def analog_to_percentage(self, adc_value, adc_min=423, adc_max=873):
        percentage = 100 * (adc_max - adc_value) / (adc_max - adc_min)
        return max(0, min(percentage, 100))

    # 土壌湿度を取得するメソッド
    def get_soil_moisture(self, channel=0, adc_min=423, adc_max=873):
        adc_value = self.read_channel(channel)
        percentage = self.analog_to_percentage(adc_value, adc_min, adc_max)
        return percentage

    # SPI接続を閉じるメソッド
    def close(self):
        self.spi.close()
