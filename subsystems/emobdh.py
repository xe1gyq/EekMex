#!/usr/bin/python

import logging
import time
from threading import Thread

from subsystems.emgps import emGps

from sensors.emaltitude import emAltitudeGet
from sensors.empressure import emPressureGet
from sensors.emsealevelpressure import emSeaLevelPressureGet
from sensors.emtemperature import emTemperatureGet

class emObdh(object):

    def __init__(self):

        logging.info('On Board Data Handling')
        thread = Thread(target=self.emObdhCapture)
        thread.start()

        self.emgpsfd = emGps()
        self.emgpsfd.emGpsPoller()

    def emObdhSensors(self):
        altitude = emAltitudeGet()
        pressure = emPressureGet()
        sealevelpressure = emSeaLevelPressureGet()
        temperature = emTemperatureGet()
        return altitude, pressure, sealevelpressure, temperature

    def emObdhGps(self):
        latitude = self.emgpsfd.emGpsAltitudeGet()
        longitude = self.emgpsfd.emGpsLongitudeGet()
        altitude = self.emgpsfd.emGpsAltitudeGet()
        return latitude, longitude, altitude

    def emObdhCapture(self):

        while True:
            altitude, pressure, sealevelpressure, temperature = self.emObdhSensors()
            sensorsdata = ("Sensors: {0}," "{1}," "{2}," "{3}".format(altitude, pressure, sealevelpressure, temperature))
            logging.info(sensorsdata)

            latitude, longitude, altitude =  self.emObdhGps()
            gpsdata = ("Gps: {0}," "{1}," "{2}".format(latitude, longitude, altitude))
            logging.info(gpsdata)

            time.sleep(5)

# End of File
