#!/usr/bin/python

import logging
from random import randint
try:
    #import pyupm_bmpx8x as upmBmpx8x
    import Adafruit_BMP.BMP085 as BMP085
except ImportError:
    pass

def emTemperatureGet(mode=None):
    if mode is None:
        #temperature = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
        #temperaturedata = temperature.getTemperature()
        sensor = BMP085.BMP085(busnum=1)
        temperaturedata = sensor.read_temperature()
    else:
        temperaturedata = randint(20,40)
    return temperaturedata

# End of File
