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


    def getFromArduino(self):
        self.ser.open()
        line1, line2 = self.ser.readline().split()

        humidity = "".join(re.findall("[0-9][0-9]+\.+[0-9][0-9]", str(line1)))
        temp = "".join(re.findall("[0-9][0-9]+\.+[0-9][0-9]", str(line2)))

        # print(humidity)
        # print(temp)
        self.closeSerialPort()
        values = {"humidity": float(humidity), "temp": float(temp)}
        return values

    def getAverage(self, times):
        sumHumi = 0
        sumTemp = 0
        singleValues = None
        print("Getting average...")

        for i in range(times):
            singleValues = self.getFromArduino()
            print(str(i + 1) + " h: " + str(singleValues["humidity"]) + ", t: " + str(singleValues["temp"]))
            sumHumi += singleValues["humidity"]
            sumTemp += singleValues["temp"]
        
        print("Done.")
        return {"humidity": float(sumHumi / times), "temp": float(sumTemp / times)}
    
    def calcTHI(self, t, h):
        thi = 0.81 * t + 0.01 * h * (0.99 * t - 14.3) + 46.3
        return thi
    
    def thiFeeling(self, thi):
        if thi < 55:
            return "寒い"
        elif thi < 60:
            return "肌寒い"
        elif thi < 65:
            return "ふつう"
        elif thi < 70:
            return "快い"
        elif thi < 75:
            return "暑くはない"
        elif thi < 80:
            return "やや暑い"
        elif thi < 85:
            return "暑くて汗が出る"
        else:
            return "暑くてたまらない"
    
    def closeSerialPort(self):
        self.ser.close()