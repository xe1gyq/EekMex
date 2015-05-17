#!/usr/bin/python

import logging
import getopt
import math
import sys
import time

import pyupm_bmpx8x as upmBmpx8x

class Bpta(object):

    def __init__(self):

        logging.info('Barometric Pressure Temperature Altitude')

        self.myBarometer = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);

    def data(self):

        while True:
            bptadata = ("Pressure {0} | "
                         "Temperature {1} | "
                         "Altitude {2} | "
                         "Sealevel {3}".format(
                         self.myBarometer.getPressure(),
                         self.myBarometer.getTemperature(),
                         self.myBarometer.getAltitude(),
                         self.myBarometer.getSealevelPressure()))

            logging.debug(bptadata)
            time.sleep(.1)

# End of File
