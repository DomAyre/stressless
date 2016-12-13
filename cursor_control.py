import stressless
import time
import random
import pyautogui as pg

sl = stressless.StressLess()
freq = 0.1
while True:
    r = sl.getSensorReading()
    randx = random.randrange(-10, 10)
    randy = random.randrange(-10, 10)
    if sl.getFrequency(6) == 2 and min([p for p in r.pressures]) > 0:
        pg.doubleClick()
    elif sl.getFrequency(6) == 1 and min([p for p in r.pressures]) > 0:
        pg.click()
    elif min([p for p in r.pressures]) < 0:
        pg.dragRel(randx, randy, duration=freq)
    else:
        pg.moveRel(randx, randy, duration=freq)
