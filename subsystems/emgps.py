#! /usr/bin/python

import logging 
import os
from gps import *
from time import *
import time
import threading
import gps
from threading import Thread

class emGps(object):

    def __init__(self):

        logging.info('Global Positioning System')
        self.gpsd = None
        self.emGpsInitialize()
        thread = Thread(target=self.emGpsPoller)
        thread.start()

    def emGpsInitialize(self):
        self.gpsd = gps.gps(mode=WATCH_ENABLE)

    def emGpsPoller(self):
        while True:
            self.gpsd.next()

    def emGpsLatitudeGet(self):
        return self.gpsd.fix.latitude

    def emGpsLongitudeGet(self):
        return self.gpsd.fix.longitude

    def emGpsAltitudeGet(self):
        return self.gpsd.fix.altitude

    def emGpsSatellitesNumberGet(self):
        return self.gpsd.satellites

# End of File
