#!/usr/bin/python

import dweepy
import json
import logging
import sys
import time

from random_words import LoremIpsum
from threading import Thread

class emDemo(object):

    def __init__(self, subsystem):

        logging.info('Demo')
        self.subsystem = subsystem

        thread = Thread(target=self.emDemoExecute)
        thread.start()

    def emDemoGps(self):

        from subsystems.emgps import emGps

        self.emgpsfd = emGps("demo")

        latitude = self.emgpsfd.emGpsLatitudeGet()
        longitude = self.emgpsfd.emGpsLongitudeGet()
        altitude = self.emgpsfd.emGpsAltitudeGet()
        gpsdata = ("Gps: {0}," "{1}," "{2}".format( \
                    latitude, longitude, altitude))
        logging.info(gpsdata)
        return latitude, longitude, altitude

    def emDemoImu(self):

        from subsystems.emimu import emImu

        self.emimu = emImu("demo")
        roll = self.emimu.emImuRollGet()
        pitch = self.emimu.emImuPitchGet()
        yaw = self.emimu.emImuYawGet()
        imudata = ("Imu: {0}," "{1}," "{2},".format(roll, pitch, yaw))
        logging.info(imudata)
        return roll, pitch, yaw

    def emDemoSensors(self):

        from sensors.emaltitude import emAltitudeGet
        from sensors.empressure import emPressureGet
        from sensors.emsealevelpressure import emSeaLevelPressureGet
        from sensors.emtemperature import emTemperatureGet

        altitude = emAltitudeGet("demo")
        pressure = emPressureGet("demo")
        sealevelpressure = emSeaLevelPressureGet("demo")
        temperature = emTemperatureGet("demo")
        sensorsdata = ("Sensors: {0}," "{1}," "{2}," "{3}".format( \
                        altitude, pressure, sealevelpressure, temperature))
        logging.info(sensorsdata)
        return altitude, pressure, sealevelpressure, temperature

    def emDemoExecute(self):

        li = LoremIpsum()

        if self.subsystem == 'all':

            while True:

                latitude, longitude, altitudegps = self.emDemoGps()
                roll, pitch, yaw = self.emDemoImu()
                altitude, pressure, sealevelpressure, temperature = self.emDemoSensors()

                data = {}
                data['alive'] = "1"
                data['altitude'] = altitude
                data['pressure'] = pressure
                data['sealevelpressure'] = sealevelpressure
                data['temperature'] = temperature
                data['roll'] = roll
                data['pitch'] = pitch
                data['yaw'] = yaw
                data['latitude'] = latitude
                data['longitude'] = longitude
                data['altitudegps'] = altitudegps 
                data['message'] = li.get_sentence()
                dweepy.dweet_for('EekMexArejXe', data)
        else:

            logging.info('Specific Demo Not Found!')

# End of File
