#!/usr/bin/python

import logging
import time
from threading import Thread

from core.emaltitude import emAltitudeGet
from core.empressure import emPressureGet
from core.emsealevelpressure import emSeaLevelPressureGet
from core.emtemperature import emTemperatureGet

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
