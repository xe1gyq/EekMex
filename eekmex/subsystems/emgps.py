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
            else:
                self.latitude = random.uniform(21.11400000, 21.11600000)
                self.longitude = random.uniform(-101.664000, -101.665000)
                self.altitude = randint(1000, 2000)

    def emGpsLatitudeGet(self):
        return self.latitude

    def emGpsLongitudeGet(self):
        return self.longitude

    def emGpsAltitudeGet(self):
        return self.altitude

    def emGpsSatellitesNumberGet(self):
        return self.gpsd.satellites

# End of File
