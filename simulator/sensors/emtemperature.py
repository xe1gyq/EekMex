#!/usr/bin/python

import logging
from random import randint

def emTemperatureGet():

    temperaturedata = randint(20,40)
    logging.info('Temperature %s' % temperaturedata)
    return temperaturedata

# End of File
