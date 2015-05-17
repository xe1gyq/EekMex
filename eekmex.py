#!/usr/bin/python

import argparse
import logging
import threading
import time

from core.alive import Alive
from core.imu import Imu
from core.bpta import Bpta

def eekMexLogging():

    # ------------------------------------------------------------
    # Base Logging Setup
    # ------------------------------------------------------------

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-2s %(module)-10s %(levelname)-4s %(message)s',
                        filename='eekmex.log',
                        filemode='a')

    # ------------------------------------------------------------
    # Logging Handlers
    # ------------------------------------------------------------

    loggerConsole = logging.StreamHandler()
    loggerConsole.setLevel(logging.INFO)

    loggerFile = logging.FileHandler('/media/sdcard/eekmex.log', 'a')
    loggerFile.setLevel(logging.DEBUG)

    # ------------------------------------------------------------
    # Logging Formatters
    # ------------------------------------------------------------

    loggerConsoleFormatter = logging.Formatter('%(name)-2s: %(module)-10s %(levelname)-4s %(message)s')
    loggerConsole.setFormatter(loggerConsoleFormatter)

    loggerFileFormatter = logging.Formatter('%(asctime)s %(name)-2s %(module)-10s %(levelname)-4s %(message)s')
    loggerFile.setFormatter(loggerFileFormatter)

    # ------------------------------------------------------------
    # Logging Handlers
    # ------------------------------------------------------------

    logging.getLogger('').addHandler(loggerFile)
    logging.getLogger('').addHandler(loggerConsole)

if __name__=='__main__':

    eekMexLogging()

    description = 'EekMex, Amateur Radio Satellite Learning Platform'
    logging.info(description)

    parser = argparse.ArgumentParser(description)
    args = parser.parse_args()

    alive = Alive()
    bpta = Bpta()
    imu = Imu()

    threadbpta = threading.Thread(name='bpta', target=bpta.data)
    threadimu = threading.Thread(name='imu', target=imu.data)

    threadbpta.daemon = True
    threadimu.daemon = True

    threadbpta.start()
    threadimu.start()

    seconds = 0

    while seconds != 15:
        alive.data()
        time.sleep(1)
        seconds += 1

# End of File
