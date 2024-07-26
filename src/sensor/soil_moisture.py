import RPi.GPIO as GPIO

# 土壌水分センサーの値を取得するクラス
class SoilMoistureSensor:
    def __init__(self, clk, miso, mosi, cs):
        self.SPICLK = clk
        self.SPIMISO = miso
        self.SPIMOSI = mosi
        self.SPICS = cs

        # GPIOの初期設定
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.SPICLK, GPIO.OUT)
        GPIO.setup(self.SPIMISO, GPIO.IN)
        GPIO.setup(self.SPIMOSI, GPIO.OUT)
        GPIO.setup(self.SPICS, GPIO.OUT)

    # MCP3008からデータを読み取るメソッド
    def read_channel(self, channel):
        if ((channel > 7) or (channel < 0)):
            return -1

        GPIO.output(self.SPICS, True)  
        GPIO.output(self.SPICLK, False)  
        GPIO.output(self.SPICS, False)  

        command = channel
        command |= 0x18
        command <<= 3

        for i in range(5):
            if (command & 0x80):
                GPIO.output(self.SPIMOSI, True)
            else:
                GPIO.output(self.SPIMOSI, False)
            command <<= 1
            GPIO.output(self.SPICLK, True)
            GPIO.output(self.SPICLK, False)

        adc_out = 0
        for i in range(12):
            GPIO.output(self.SPICLK, True)
            GPIO.output(self.SPICLK, False)
            adc_out <<= 1
            if (GPIO.input(self.SPIMISO)):
                adc_out |= 0x1

        GPIO.output(self.SPICS, True)
        
        adc_out >>= 1
        return adc_out

    # 土壌湿度をパーセンテージに変換
    def analog_to_percentage(self, adc_value, adc_min=423, adc_max=873):
        percentage = 100 * (adc_value - adc_min) / (adc_max - adc_min)
        return max(0, min(percentage, 100))

    # GPIOのクリーンアップ
    def cleanup(self):
        GPIO.cleanup()

