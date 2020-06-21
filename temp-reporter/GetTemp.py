# ライブラリ pySerialを使用
import serial
import re

class GetTemp:
    ser = None
    def __init__(self, port, rate):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = rate
        self.ser.setDTR(False)
        self.ser.open()


    def getFromArduino(self):
        line1, line2 = self.ser.readline().split()

        humidity = "".join(re.findall("[0-9][0-9]+\.+[0-9][0-9]", str(line1)))
        temp = "".join(re.findall("[0-9][0-9]+\.+[0-9][0-9]", str(line2)))

        # print(humidity)
        # print(temp)

        values = {"humidity": float(humidity), "temp": float(temp)}
        return values
    
    def closeSerialPort(self):
        self.ser.close()