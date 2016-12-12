import serial
import re
import code
import os
import sys
from sys import platform


class ArduinoInterface:
    def __init__(self, devFile=""):
        # For Joy's MBP, device file is /dev/cu.usbmodem1411
        if not devFile:
            devFile = self._discoverDevice()
        self.ser = serial.Serial(devFile, 9600, timeout=1);

        # Clear buffered things before starting afresh
        self.ser.reset_input_buffer()

    def getData(self):

        self.line = self.ser.readline()

        # Line contains newline char
        self.line = self.line[0:-1]

        while len(self.line) == 0:
            self.line = self.ser.readline()
            self.line = self.line[0:-1]

        # Do something with line, e.g.
        # print(self.line)

        return self.line

        # code.interact(local=dict(globals(), **locals()))

    def _discoverDevice(self):
        if platform == "linux" or platform == "darwin" or platform == "linux2":
            files = os.listdir("/dev/")
            r = re.compile("cu.usb.*")
            devFile = "/dev/" + [m for m in files if r.match(m)][0]
            print("The dev file is:", devFile)
        else:
            raise Exception("device file must be specified for windows")
        return devFile
