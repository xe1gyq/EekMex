#!/usr/bin/python

import logging
import pyupm_bmpx8x as upmBmpx8x

def emPressureGet():

    pressure = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
    pressuredata = pressure.getPressure()
    logging.debug('Pressure %s' % pressuredata)
    return pressuredata

# End of File
