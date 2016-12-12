import arduinoInterface as ard
import sys

interface = ard.ArduinoInterface()
while True:
    print(interface.getData())