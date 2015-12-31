#!/usr/bin/python

import logging
from random import randint
try:
    #import pyupm_bmpx8x as upmBmpx8x
    import Adafruit_BMP.BMP085 as BMP085
except ImportError:
    pass

def emSeaLevelPressureGet(mode=None):

    if mode is None:
        #sealevelpressure = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
        #sealevelpressuredata = sealevelpressure.getSealevelPressure()
        sensor = BMP085.BMP085(busnum=1)
        sealevelpressuredata = sensor.read_sealevel_pressure()
    else:
        sealevelpressuredata = randint(1000,2000)
    logging.info('Sea Level Pressure %s' % sealevelpressuredata)
    return sealevelpressuredata

# End of File
