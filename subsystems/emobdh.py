#!/usr/bin/python

import logging
import time
from threading import Thread

from sensors.emaltitude import emAltitudeGet
from sensors.empressure import emPressureGet
from sensors.emsealevelpressure import emSeaLevelPressureGet
from sensors.emtemperature import emTemperatureGet

class emOnBoardDataHandling(object):

    def __init__(self):

        logging.info('On Board Data Handling')
        thread = Thread(target=self.emObdhCapture)
        thread.start()

    def emObdhCapture(self):
        while True:
            altitude = emAltitudeGet()
            pressure = emPressureGet()
            sealevelpressure = emSeaLevelPressureGet()
            temperature = emTemperatureGet()
            data = ("{0}," "{1}," "{2}," "{3}".format(altitude, pressure, sealevelpressure, temperature))
            logging.info(data)
            time.sleep(5)

# End of File
