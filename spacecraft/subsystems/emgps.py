#! /usr/bin/python

import logging 
import os
from gps import *
import random
from random import randint
from time import *
import time
import threading
import gps
from threading import Thread

class emGps(object):

    def __init__(self, mode=None):

        logging.info('Global Positioning System')
        self.gpsd = None
        self.mode = mode
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.satellites = None

        if mode is None:
            self.emGpsInitialize()

        thread = Thread(target=self.emGpsPoller)
        thread.start()

    def emGpsInitialize(self):
        self.gpsd = gps.gps(mode=WATCH_ENABLE)

    def emGpsPoller(self):
        while True:
            if self.mode is None:
                self.gpsd.next()
                self.latitude = self.gpsd.fix.latitude
                self.longitude = self.gpsd.fix.longitude
                self.altitude = self.gpsd.fix.altitude
                self.satellites = self.gpsd.satellites
            else:
                self.latitude = random.uniform(21.14000000, 21.18000000)
                self.longitude = random.uniform(-101.600000, -101.660000)
                self.altitude = randint(1000, 2000)
                self.satellites = randint(1,10)

    def emGpsData(self):
        gpsdata = ("Gps: {0}," "{1}," "{2}".format( \
                    self.latitude, self.longitude, self.altitude, self.satellites))
        logging.info(gpsdata)
        return self.latitude, self.longitude, self.altitude, self.satellites

    def emGpsLatitude(self):
        return self.latitude

    def emGpsLongitude(self):
        return self.longitude

    def emGpsAltitude(self):
        return self.altitude

    def emGpsSatellites(self):
        return self.satellites

# End of File
