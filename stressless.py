import time
import multiprocessing as mp
from supportFunctions import *
from stressmodel import StressModel, Reading


class StressLess():
    def __init__(self):
        self.device = StressModel()
        self.activeProcesses = []

    def getSensorReading(self):
        return self.device.getReadings(1)[0]

    def getAverageReading(self, number_of_readings=0):

        if number_of_readings == 0:
            avgReading = self.device.getSessionAvgReadings()
        else:
            readings = self.device.getReadings(number_of_readings)
            avg = [0 for _ in range(len(readings[0].pressure) + 1)]
            for reading in readings:
                avg[0] += reading.time
                for j, el2 in enumerate(reading.pressure):
                    avg[j + 1] += el2.pressure
            avg = [a/len(readings) for a in avg]
            avgReading = Reading(avg)
        return avgReading

    def getFrequency(self, number_of_readings=25):
        readings = self.device.getReadings(number_of_readings)
        time = readings[0].Time() - readings[-1].Time()
        threshold = self.device.getPressureThreshold()

        number_of_squeezes = 0
        activated = False
        for reading in readings:
            if not activated and max(reading.pressure) > threshold:
                activated = True
                number_of_squeezes += 1
            if activated and max(reading.pressure) < threshold:
                activated = False
        return number_of_squeezes / time

    def getGripStrength(self, frequency=-1):
        pass

    def getPalmConfig(self, frequency=-1):
        reading = self.device.getReadings(1)[0]
        threshold = self.device.getReadingFrequency()
        configuration = [p > threshold for p in reading.pressure]
        return configuration

    def getStressLevel(self, frequency=-1):
        # get
        pass

    def learn(self, stressLevel, sensorReading=False):
        if not sensorReading:
            sensorReading = self.device.getReadings(1)
        pass

    def adjust_threshold(self, squeeze_pressure_readings, non_squeeze_pressure_readings):
        avg_squeeze_reading = sum(sum(r) for r in squeeze_pressure_readings)
        avg_non_squeeze_reading = sum(sum(r) for r in non_squeeze_pressure_readings)
        self.device.setPressureThreshold((avg_squeeze_reading + avg_non_squeeze_reading) / 2)

    # OUTPUT

    def setLED(self, red, green, blue, alpha):
        pass

    def turnOn(self):
        pass

    def turnOff(self):
        pass

    def setSensorFrequency(self, frequency):
        self.device.setReadingFrequency()