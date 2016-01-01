#!/usr/bin/python

import dweepy
import logging
import time
import serial

class emTelemetry(object):

    def __init__(self, device):
        logging.info('Telemetry')
        self.device = device
        if self.device is "dweetio":
            pass
        elif self.device is "xbee":
            self.serial = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

    def emTelemetryDweetIo(self, data):
        try:
            dweepy.dweet_for('EekMexSpacecraft', data)
        except (StopIteration, KeyboardInterrupt, SystemExit):
            pass

        #logging.info(data)
        #self.serial.write('%s\n' % data)
        #line = self.serial.readline()
        #logging.info(data)

# End of File
