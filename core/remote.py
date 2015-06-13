
#!/usr/bin/python

import logging
from xbee import XBee
import serial

from system import System

class Remote(object):

    def __init__(self):

        logging.info('Core Remote')
        self.remote = serial.Serial('/dev/ttyUSB0', 9600)
        xbee = XBee(self.remote)

    def close(self):

        self.remote.close()

    def send(self):

        self.remote.write("EekMex Remote Test\n")

# End of File
