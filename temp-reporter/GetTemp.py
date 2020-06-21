# ライブラリ pySerialを使用
import serial

class GetTemp:
    def __init__(self, port, rate):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = rate
        self.ser.setDTR(False)
        self.ser.open()


    def getFromArduino(self):
        line = self.ser.readLine()
        values = list(float(line.split()))
        return values
    
    def closeSerialPort(self):
        self.ser.close()