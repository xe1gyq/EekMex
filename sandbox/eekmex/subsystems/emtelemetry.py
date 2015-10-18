#!/usr/bin/python

import logging
import time
import serial

class emTelemetry(object):

    def __init__(self):

        logging.info('Telemetry')
        self.serial = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

    def emTelemetrySend(self, data):

        logging.info(data)
        #self.serial.write('%s\n' % data)
        #line = self.serial.readline()
        #logging.info(data)

# End of File
