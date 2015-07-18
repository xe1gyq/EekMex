#!/usr/bin/python

import logging
#import pyupm_bmpx8x as upmBmpx8x
import Adafruit_BMP.BMP085 as BMP085

def emPressureGet():

    #pressure = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
    #pressuredata = pressure.getPressure()
    sensor = BMP085.BMP085()
    pressuredata = sensor.read_pressure()
    logging.info('Pressure %s' % pressuredata)
    return pressuredata

# End of File
