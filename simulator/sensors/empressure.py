#!/usr/bin/python

import logging
from random import randint

def emPressureGet():

    pressuredata = randint(1000,2000)
    logging.info('Pressure %s' % pressuredata)
    return pressuredata

# End of File
