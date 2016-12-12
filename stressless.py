import time
from supportFunctions import *
from stressmodel import StressModel, Reading
import os
import csv
import requests
from collections import defaultdict


class StressLevel():
    """
    format is: stress level, [pressure readings]
    example: 2, 10, 30, 30, 20
    """
    def __init__(self, filename):
        self.learn_file = filename
        self.model = self._readFileIntoModel(self, filename)
        self.averageModel = self._getModelAverage()

    def _readFileIntoModel(self, filename):
        model = defaultdict()
        with open(filename, 'rb') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            print(data)  # debugging
        for d in data:
            model[d[0]].append(tuple(d[1:]))
        return model

    def _getModelAverage(self):
        average_model = defaultdict()
        for k in self.model:
            average_model[k] = sum([v for v in self.model[k]]) / len(self.model[k])
        return average_model

    def saveModel(self, filename=False):
        if not filename:
            filename = self.learn_file
        data = [str(k) + "," + ",".join(v) for (k, v) in self.model]
        with open(filename, 'wb') as csvfile:
            csvfile.writelines("\n".join(data) + "\n")

    def addReading(self, stressLevel, pressures):
        self.model[stressLevel] = self.model[stressLevel] + tuple(pressures)


class StressLess():
    def __init__(self, filename="temp.learn"):
        self._device = StressModel()
        # self._stressLevelModel = StressLevel(filename)

    def getSensorReading(self):
        return self._device.getReadings(1)[0]

    def getAverageReading(self, number_of_readings=0):

        if number_of_readings == 0:
            avgReading = self._device.getSessionAvgReadings()
        else:
            readings = self._device.getReadings(number_of_readings)
            avg = [0 for _ in range(len(readings[0].pressure) + 1)]
            for reading in readings:
                avg[0] += reading.time
                for j, el2 in enumerate(reading.pressure):
                    avg[j + 1] += el2.pressure
            avg = [a/len(readings) for a in avg]
            avgReading = Reading(avg)
        return avgReading

    def getFrequency(self, number_of_readings=100):
        readings = self._device.getReadings(number_of_readings)
        time = readings[-1].time - readings[0].time + 1
        threshold = self._device.getPressureThreshold()

        number_of_squeezes = 0
        activated = False
        for reading in readings:
            if not activated and min(reading.pressure) > threshold:
                activated = True
                number_of_squeezes += 1
            if activated and min(reading.pressure) < threshold:
                activated = False
        frequency = 1000 * (number_of_squeezes / time)
        print(frequency)
        return 1000 * (number_of_squeezes / time)

    def getGripStrength(self, frequency=-1):
        pass

    def getPalmConfig(self, frequency=-1):
        reading = self._device.getReadings(1)[0]
        threshold = self._device.getReadingFrequency()
        configuration = [p > threshold for p in reading.pressure]
        return configuration

    def getStressLevel(self, frequency=-1):
        # get closest reading and matching stress Level from learn

        pass

    def learn(self, stress_level, sensor_reading=False):
        assert(stress_level <= 5 and sensor_reading >= 1)
        if not sensor_reading:
            sensor_reading = self._device.getReadings(1)
        pass

    def adjust_threshold(self, custom=False, squeeze_pressure_readings=False, non_squeeze_pressure_reading=False):
        if custom:
            self._device.setPressureThreshold((custom))
        elif squeeze_pressure_readings and non_squeeze_pressure_reading:
            try:
                avg_squeeze_reading = sum(sum(r) for r in squeeze_pressure_readings)
                avg_non_squeeze_reading = sum(sum(r) for r in non_squeeze_pressure_reading)
                self._device.setPressureThreshold((avg_squeeze_reading + avg_non_squeeze_reading) / 2)
            except TypeError:
                print("Threshold not set. \
                Format of pressure readings must be a list of lists containing numerical values.")

    # OUTPUT

    def turnOn(self):
        pass

    def turnOff(self):
        pass

    def setSensorFrequency(self, frequency):
        self._device.setReadingFrequency()

    def sendIFTT(self, command="turns_on", payload=(), key="dKx0NTPTbFi1jLPW3MlCxA"):
        if not payload:
            payload = []
        elif len(payload) > 3:
            raise Exception('payload has to have up to 3 arguments')
        requests.post("https://maker.ifttt.com/trigger/{command}/with/key/{key}", data=payload)