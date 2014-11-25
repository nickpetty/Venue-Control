import serial
import time

# [chnl]c[value]w ie 1c255w

class EDYC2DMX():
    def __init__(self, port):
        self.ser = serial.Serial(int(port), baudrate=115200)
        time.sleep(1.6)

    def send(self, channel, value):
        packet = str(channel-1) + "c" + str(value) + "w"
        self.ser.write(packet)

    def fade(self):
        for i in xrange(0,255,5):
            self.ser.write("7c" + str(i) + "w")
            time.sleep(.1)

#dmx = EDYC2DMX(23)
#dmx.send(8,0)
#dmx.fade()

