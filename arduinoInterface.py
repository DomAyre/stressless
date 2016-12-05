import serial
import code
import os
import sys

class ArduinoInterface:
    def __init__(self, devFile):
        # For Joy's MBP, device file is /dev/cu.usbmodem1411

        with serial.Serial(devFile, 9600, timeout=1) as ser:
            # Clear buffered things before starting afresh
            ser.reset_input_buffer()

    def getData(self):
        
        self.line = ser.readline()

        # Line contains newline char
        self.line = line[0:-1]

        if len(self.line) == 0:
            return

        # Do something with line, e.g.
        print(self.line)

        cmd = 'CMD_NUMBER\n'
        data = '1337\n'

        # Maybe send something to Arduino
        ser.write(cmd)
        ser.write(data)

        return line

        # code.interact(local=dict(globals(), **locals()))

