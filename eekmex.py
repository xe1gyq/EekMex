#!/usr/bin/python

import argparse
import logging
import sys
import threading
import time

from subsystems.emobdh import emObdh

from core.alive import Alive
from core.imu import Imu
from core.remote import Remote

def eekMexLogging():

    # ------------------------------------------------------------
    # Base Logging Setup
    # ------------------------------------------------------------

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-2s %(module)-10s %(levelname)-4s %(message)s',
                        filename='eekmex.log',
                        filemode='a')

    # ------------------------------------------------------------
    # Logging Handlers
    # ------------------------------------------------------------

    loggerConsole = logging.StreamHandler()
    loggerConsole.setLevel(logging.INFO)

    loggerFile = logging.FileHandler('/media/sdcard/eekmex.log', 'a')
    loggerFile.setLevel(logging.INFO)

    loggerFileGoogleEarth = logging.FileHandler('/media/sdcard/eekmexprekml.log', 'a')
    loggerFileGoogleEarth.setLevel(logging.WARNING)

    # ------------------------------------------------------------
    # Logging Formatters
    # ------------------------------------------------------------

    loggerConsoleFormatter = logging.Formatter('%(name)-2s: %(module)-10s %(levelname)-4s %(message)s')
    loggerConsole.setFormatter(loggerConsoleFormatter)

    loggerFileFormatter = logging.Formatter('%(asctime)s %(name)-2s %(module)-10s %(levelname)-4s %(message)s')
    loggerFile.setFormatter(loggerFileFormatter)

    loggerFileGoogleEarthFormatter = logging.Formatter('%(process)d %(asctime)s %(message)s', datefmt="%d %m %Y %H %M %S ")
    loggerFileGoogleEarth.setFormatter(loggerFileGoogleEarthFormatter)

    # ------------------------------------------------------------
    # Logging Handlers
    # ------------------------------------------------------------

    logging.getLogger('').addHandler(loggerConsole)
    logging.getLogger('').addHandler(loggerFile)
    logging.getLogger('').addHandler(loggerFileGoogleEarth)

if __name__=='__main__':

    eekMexLogging()

    description = 'EekMex, Amateur Radio Satellite Learning Platform'
    logging.info(description)

    parser = argparse.ArgumentParser(description)
    args = parser.parse_args()

    obdh = emObdh()

    while True:

        time.sleep(1)

    sys.exit(0)

    alive = Alive()
    imu = Imu()
    remote = Remote()

    threadimu = threading.Thread(name='imu', target=imu.data)

    threadimu.daemon = True

    threadimu.start()

    seconds = 0

    while seconds != 5:
        alive.data()
        time.sleep(1)
        seconds += 1
        remote.send()

    remote.close()

# End of File
