#!/usr/bin/python

import logging
import pyupm_bmpx8x as upmBmpx8x

def emTemperatureGet():

    temperature = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
    temperaturedata = temperature.getTemperature()
    logging.info('Temperature %s' % temperaturedata)
    return temperaturedata

# End of File
