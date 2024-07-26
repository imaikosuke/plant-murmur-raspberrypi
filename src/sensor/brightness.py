import RPi.GPIO as GPIO
from time import sleep

# 照度センサーの値を取得するクラス
class BrightnessSensor:
    def __init__(self, clockpin, mosipin, misopin, cspin):
        self.clockpin = clockpin
        self.mosipin = mosipin
        self.misopin = misopin
        self.cspin = cspin
        self.pin_initilized = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clockpin, GPIO.OUT)
        GPIO.setup(self.mosipin, GPIO.OUT)
        GPIO.setup(self.misopin, GPIO.IN)
        GPIO.setup(self.cspin, GPIO.OUT)
        self.pin_initilized = True

    # MCP3008からデータを読み取るメソッド
    def readadc(self, adcnum):
        if adcnum > 7 or adcnum < 0:
            return -1
        GPIO.output(self.cspin, GPIO.HIGH)
        GPIO.output(self.clockpin, GPIO.LOW)
        GPIO.output(self.cspin, GPIO.LOW)
        commandout = adcnum
        commandout |= 0x18
        commandout <<= 3
        for i in range(5):
            if commandout & 0x80:
                GPIO.output(self.mosipin, GPIO.HIGH)
            else:
                GPIO.output(self.mosipin, GPIO.LOW)
            commandout <<= 1
            GPIO.output(self.clockpin, GPIO.HIGH)
            GPIO.output(self.clockpin, GPIO.LOW)
        adcout = 0
        for i in range(13):
            GPIO.output(self.clockpin, GPIO.HIGH)
            GPIO.output(self.clockpin, GPIO.LOW)
            adcout <<= 1
            if i > 0 and GPIO.input(self.misopin) == GPIO.HIGH:
                adcout |= 0x1
        GPIO.output(self.cspin, GPIO.HIGH)
        return adcout

    # ３つの照度センサー値の最大値を取得するメソッド
    def get_brightness(self):
        inputVal0 = self.readadc(0)
        inputVal1 = self.readadc(1)
        inputVal2 = self.readadc(2)
        maxVal = max(inputVal0, inputVal1, inputVal2)
        return maxVal

    # GPIOのクリーンアップ
    def cleanup(self):
        if self.pin_initilized:
            GPIO.cleanup()
