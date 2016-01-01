#!/usr/bin/python

import json
import logging
import sys
import time

from subsystems.emgps import emGps
from subsystems.emimu import emImu
from subsystems.emsensors import emSensors
from subsystems.emtelemetry import emTelemetry

from random_words import LoremIpsum
from threading import Thread

class emVirtual(object):

    def __init__(self):

        logging.info('Spacecraft Virtual')
        self.mode = "virtual"

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
        self.speed = None
        self.track = None

        self.li = LoremIpsum()
        self.emgpsfd = emGps(self.mode)
        self.emimu = emImu(self.mode)
        self.emsensors = emSensors(self.mode)
        self.emtelemetry = emTelemetry(self.mode)

        threadDemoExecute = Thread(target=self.emVirtualExecute)
        threadDemoExecute.start()

        threadDemoTelemetry = Thread(target=self.emVirtualTelemetry)
        threadDemoTelemetry.start()

    def emVirtualExecute(self):
        self.emgpsfd.start()
        try:
            while True:
                self.latitude, self.longitude, self.altitudegps, self.satellites, self.speed, self.track = self.emgpsfd.emGpsData()
                self.roll, self.pitch, self.yaw = self.emimu.emImuData()
                self.altitude, self.pressure, self.sealevelpressure, self.temperature = self.emsensors.emSensorsData()
                time.sleep(1)
        except (StopIteration, KeyboardInterrupt, SystemExit):
            pass

    def emVirtualTelemetry(self):
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
                data['speed'] =  self.speed
                data['track'] =  self.track
                data['message'] = self.li.get_sentence()
                self.emtelemetry.emTelemetryDweetIo(data)
                time.sleep(1)
        except (StopIteration, KeyboardInterrupt, SystemExit):
            pass

    def emVirtualRecord(self):
        datage = ("{0} " "{1} " "{2} " "{3} " \
                  "{4} " "{5} " "{6} " "{6} ".format(
                  self.latitude, self.longitude, self.altitude, self.pressure, \
                  self.temperature, self.roll, self.pitch, self.yaw))
        logging.warning(datage)

# End of File
