#!/usr/bin/python

import logging
import time
import serial

class emTelemetry(object):

    def __init__(self):

        logging.info('Telemetry')

        self.serial = serial.Serial('/dev/ttyUSB0', 9600)

    def emTelemetrySend(self, data):

        self.serial.write('%s\n' % data)
        time.sleep(5)

# End of File
