#!/usr/bin/python

import dweepy
import json
import logging
import sys
import time

from subsystems.emgps import emGps
from subsystems.emimu import emImu
from subsystems.emsensors import emSensors

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
        self.satellites = None

        self.li = LoremIpsum()
        self.emgpsfd = emGps("demo")
        self.emimu = emImu("demo")
        self.emsensors = emSensors("demo")

        threadDemoExecute = Thread(target=self.emDemoExecute)
        threadDemoExecute.start()

        threadDemoDweet = Thread(target=self.emDemoDweet)
        threadDemoDweet.start()

    def emDemoExecute(self):
        self.emgpsfd.start()
        try:
            while True:
                self.latitude, self.longitude, self.altitudegps, self.satellites = self.emgpsfd.emGpsData()
                self.roll, self.pitch, self.yaw = self.emimu.emImuData()
                self.altitude, self.pressure, self.sealevelpressure, self.temperature = self.emsensors.emSensorsData()
                time.sleep(1)
        except (StopIteration, KeyboardInterrupt, SystemExit):
            pass

    def emDemoDweet(self):
        try:
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
                data['satellites'] = self.satellites
                data['message'] = self.li.get_sentence()
                dweepy.dweet_for('EekMexArejXe', data)
                time.sleep(1)
        except (StopIteration, KeyboardInterrupt, SystemExit):
            pass

# End of File
