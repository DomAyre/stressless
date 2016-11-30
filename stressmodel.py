class Reading():
    def __init__(self, data):
        self.time = data[0]
        self.pressure = list(data[0])  # list

    def add(self, reading):
        self.time += reading[0]
        for i, el in enumerate(self.pressure):
            self.pressure[i] += reading.pressure[i]

    def divide(self, divisor):
        self.time /= divisor
        for el in self.pressure:
            self.pressure /= divisor


class StressModel():
    def __init__(self):
        self.data = []  # list of Reading objects
        self.average = []
        self.frequency = 1
        self.threshold = 0

    def readData(self):
        current_size = len(self.data)
        data = [0, [0, 30, 10]]  # placeholder for the future. Should read data from device
        reading = Reading(data)
        self.data += reading
        self.average = self.average.add(reading).divide((current_size + 1) / current_size)

    def getSessionAvgReadings(self):
        return self.average

    def set_average(self):
        self.average = sum(self.data)/len(self.data)

    def getReadings(self, number_of_readings):
        if number_of_readings > len(self.data):
            number_of_readings = len(self.data)
        return self.data[number_of_readings:]

    def getReadingFrequency(self):
        return self.frequency

    def setReadingFrequency(self, frequency):
        self.frequency = frequency

    def setPressureThreshold(self, threshold):
        self.threshold = threshold

    def getPressureThreshold(self):
        return self.threshold


