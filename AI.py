import arduinoInterface as AI
ai = AI.ArduinoInterface("/dev/cu.usbmodem10")
while 1:
     print ai.getData()
