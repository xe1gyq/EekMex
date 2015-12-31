#!/usr/bin/python

import logging
from random import randint
try:
    #import pyupm_bmpx8x as upmBmpx8x
    import Adafruit_BMP.BMP085 as BMP085
except ImportError:
    pass

def emAltitudeGet(mode=None):

    if mode is None:
        #altitude = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
        #altitudedata = altitude.getAltitude()
        sensor = BMP085.BMP085(busnum=1)
        altitudedata = sensor.read_altitude()
    else:
        altitudedata = randint(2000,3000)
    logging.info('Altitude %s' % altitudedata)
    return altitudedata

# End of File
