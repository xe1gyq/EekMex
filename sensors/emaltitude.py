#!/usr/bin/python

import logging
import pyupm_bmpx8x as upmBmpx8x

def emAltitudeGet():

    altitude = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
    altitudedata = altitude.getAltitude()
    logging.debug('Altitude %s' % altitudedata)
    return altitudedata

# End of File
