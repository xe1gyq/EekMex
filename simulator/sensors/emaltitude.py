#!/usr/bin/python

import logging
from random import randint

def emAltitudeGet():

    altitudedata = randint(2000,3000)
    logging.info('Altitude %s' % altitudedata)
    return altitudedata

# End of File
