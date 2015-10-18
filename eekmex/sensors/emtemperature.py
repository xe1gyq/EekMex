#!/usr/bin/python

import logging
import pyupm_bmpx8x as upmBmpx8x
import Adafruit_BMP.BMP085 as BMP085

def emTemperatureGet():

    #temperature = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
    #temperaturedata = temperature.getTemperature()
    sensor = BMP085.BMP085()
    temperaturedata = sensor.read_temperature()
    logging.info('Temperature %s' % temperaturedata)
    return temperaturedata

# End of File
