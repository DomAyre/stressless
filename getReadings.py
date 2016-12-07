import arduinoInterface as ard
import sys

interface = ard.ArduinoInterface(sys.argv[1])
while True:
    print(interface.getData())