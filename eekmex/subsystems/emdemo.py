#!/usr/bin/python

import dweepy
import json
import logging
import sys
import time

from subsystems.emgps import emGps
from subsystems.emimu import emImu
from sensors.emaltitude import emAltitudeGet
from sensors.empressure import emPressureGet
from sensors.emsealevelpressure import emSeaLevelPressureGet
from sensors.emtemperature import emTemperatureGet

from random_words import LoremIpsum
from threading import Thread

class emDemo(object):

    def __init__(self):

        logging.info('Demo')

        self.altitude = None
        self.temperature = None
        self.sealevelpressure = None
        self.pressure = None
        self.roll = None
        self.pitch = None
        self.yaw = None
        self.latitude = None
        self.longitude = None
        self.altitudegps = None

        self.li = LoremIpsum()
        self.emgpsfd = emGps("demo")
        self.emimu = emImu("demo")

        threadDemoExecute = Thread(target=self.emDemoExecute)
        threadDemoExecute.start()

        threadDemoDweet = Thread(target=self.emDemoDweet)
        threadDemoDweet.start()

    def emDemoGps(self):
        self.latitude = self.emgpsfd.emGpsLatitudeGet()
        self.longitude = self.emgpsfd.emGpsLongitudeGet()
        self.altitudegps = self.emgpsfd.emGpsAltitudeGet()
        gpsdata = ("Gps: {0}," "{1}," "{2}".format( \
                    self.latitude, self.longitude, self.altitudegps))
        logging.info(gpsdata)

    def emDemoImu(self):
        self.roll = self.emimu.emImuRollGet()
        self.pitch = self.emimu.emImuPitchGet()
        self.yaw = self.emimu.emImuYawGet()
        imudata = ("Imu: {0}," "{1}," "{2},".format(self.roll, self.pitch, self.yaw))
        logging.info(imudata)

    def emDemoSensors(self):
        self.altitude = emAltitudeGet("demo")
        self.pressure = emPressureGet("demo")
        self.sealevelpressure = emSeaLevelPressureGet("demo")
        self.temperature = emTemperatureGet("demo")
        sensorsdata = ("Sensors: {0}," "{1}," "{2}," "{3}".format( \
                        self.altitude, self.pressure, self.sealevelpressure, self.temperature))
        logging.info(sensorsdata)

    def emDemoExecute(self):
        while True:
            self.emDemoGps()
            self.emDemoImu()
            self.emDemoSensors()

    def emDemoDweet(self):
        while True:
            data = {}
            data['alive'] = "1"
            data['altitude'] = self.altitude
            data['pressure'] = self.pressure
            data['sealevelpressure'] = self.sealevelpressure
            data['temperature'] = self.temperature
            data['roll'] = self.roll
            data['pitch'] = self.pitch
            data['yaw'] = self.yaw
            data['latitude'] = self.latitude
            data['longitude'] = self.longitude
            data['altitudegps'] = self.altitudegps 
            data['message'] = self.li.get_sentence()
            dweepy.dweet_for('EekMexArejXe', data)

# End of File
