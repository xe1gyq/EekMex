#!/usr/bin/python

import logging
import pyupm_bmpx8x as upmBmpx8x

def emSeaLevelPressureGet():

    sealevelpressure = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
    sealevelpressuredata = sealevelpressure.getSealevelPressure()
    logging.info('Sea Level Pressure %s' % sealevelpressuredata)
    return sealevelpressuredata

# End of File
