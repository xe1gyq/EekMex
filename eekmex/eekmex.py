#!/usr/bin/python

import argparse
import logging
import os
import sys
import threading
import time

from subsystems.emobdh import emObdh
from subsystems.emdemo import emDemo

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

    description = 'EekMex, Aerospace Learning Platform'
    logging.info(description)

    parser = argparse.ArgumentParser(description)
    parser.add_argument('-c', '--clean', help='Mode Clean Up')
    parser.add_argument('-d', '--demo', help='Mode Demo')
    parser.add_argument('-p', '--project', help='Mode Project')
    args = parser.parse_args()

    if args.clean == 'files':

        logging.info('Mode Clean Up, Remove Files')

        os.remove('eekmex.log')
        os.remove('/media/sdcard/eekmex.log')
        os.remove('/media/sdcard/eekmexprekml.log')

    if args.demo == 'imu':

        logging.info('Mode Demo, IMU')
        emdemo = emDemo('imu')
        while True:
            emdemo.emDemoExecute()

    if args.demo == 'sensors':

        logging.info('Mode Demo, Sensors')
        emdemo = emDemo('sensors')
        while True:
            emdemo.emDemoExecute()

    if args.project == '0x01':

        logging.info('Mode Project, 0x01')

# End of File
