#!/usr/bin/python

import logging
#import pyupm_bmpx8x as upmBmpx8x
import Adafruit_BMP.BMP085 as BMP085

def emAltitudeGet():

    #altitude = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
    #altitudedata = altitude.getAltitude()
    sensor = BMP085.BMP085(busnum=1)
    altitudedata = sensor.read_altitude()
    logging.info('Altitude %s' % altitudedata)
    return altitudedata

# End of File
