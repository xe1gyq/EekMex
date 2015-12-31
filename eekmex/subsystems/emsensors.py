#! /usr/bin/python

import logging 
import os

from sensors.emaltitude import emAltitudeGet
from sensors.empressure import emPressureGet
from sensors.emsealevelpressure import emSeaLevelPressureGet
from sensors.emtemperature import emTemperatureGet
from threading import Thread

class emSensors(object):

    def __init__(self, mode=None):

        logging.info('Sensors')

        self.mode = mode
        self.altitude = None
        self.temperature = None
        self.sealevelpressure = None
        self.pressure = None

        thread = Thread(target=self.emSensorsPoller)
        thread.start()

    def emSensorsPoller(self):
        while True:
            self.altitude = emAltitudeGet("demo")
            self.pressure = emPressureGet("demo")
            self.sealevelpressure = emSeaLevelPressureGet("demo")
            self.temperature = emTemperatureGet("demo")

    def emSensorsData(self):
        sensorsdata = ("Sensors: {0}," "{1}," "{2}," "{3}".format( \
                        self.altitude, self.pressure, self.sealevelpressure, self.temperature))
        logging.info(sensorsdata)
        return self.altitude, self.pressure, self.sealevelpressure, self.temperature

# End of File
