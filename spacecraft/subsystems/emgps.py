#! /usr/bin/python

import logging 
import os
import random
import threading

from random import randint

class emGps(threading.Thread):

    def __init__(self, mode=None):
        threading.Thread.__init__(self)
        logging.info('Global Positioning System')

        self.gpsd = None
        self.running = False

        self.mode = mode
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.satellites = None

        if self.mode is None:
            self.gpsd = gps.gps(mode=WATCH_ENABLE)

    def run(self):
        self.running = True
        while self.running:
            if self.mode is None:
                self.gpsd.next()

    def stop(self):
        self.running = False

    def emGpsData(self):
        if self.mode is None:
            self.latitude = self.gpsd.fix.latitude
            self.longitude = self.gpsd.fix.longitude
            self.altitude = self.gpsd.fix.altitude
            self.satellites = self.gpsd.satellites
        else:
            self.latitude = random.uniform(21.14000000, 21.18000000)
            self.longitude = random.uniform(-101.600000, -101.660000)
            self.altitude = randint(1000, 2000)
            self.satellites = randint(1,10)

        gpsdata = ("Gps: {0}," "{1}," "{2}".format( \
                    self.latitude, self.longitude, self.altitude, self.satellites))
        logging.info(gpsdata)
        return self.latitude, self.longitude, \
               self.altitude, self.satellites \

    @property
    def fix(self):
        return self.gpsd.fix

    @property
    def utc(self):
        return self.gpsd.utc

    @property
    def satellitess(self):
        return self.gpsd.satellites

# End of File
