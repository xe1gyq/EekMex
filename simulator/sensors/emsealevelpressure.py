#!/usr/bin/python

import logging
from random import randint

def emSeaLevelPressureGet():

    sealevelpressuredata = randint(1000,2000)
    logging.info('Sea Level Pressure %s' % sealevelpressuredata)
    return sealevelpressuredata

# End of File
