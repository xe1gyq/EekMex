#!/usr/bin/python

import logging
from random import randint
try:
    #import pyupm_bmpx8x as upmBmpx8x
    import Adafruit_BMP.BMP085 as BMP085
except ImportError:
    pass

def emPressureGet(mode=None):

    if mode is None:
        #pressure = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
        #pressuredata = pressure.getPressure()
        sensor = BMP085.BMP085(busnum=1)
        pressuredata = sensor.read_pressure()
    else:
        pressuredata = randint(1000,2000)
    return pressuredata

# End of File
