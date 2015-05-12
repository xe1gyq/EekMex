#!/usr/bin/python

import argparse
import logging
import time

from core.alive import Alive
from core.imu import Imu

def eekMexLogging():

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-2s %(module)-10s %(levelname)-4s %(message)s',
                        #datefmt='%m-%d %H:%M',
                        filename='/media/sdcard/eekmex.log',
                        filemode='a')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    formatter = logging.Formatter('%(name)-2s: %(module)-10s %(levelname)-4s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

if __name__=='__main__':

    eekMexLogging()

    description = 'EekMex, Amateur Radio Satellite Learning Platform'
    logging.info(description)

    parser = argparse.ArgumentParser(description)
    args = parser.parse_args()

    imu = Imu()
    alive = Alive()

    while True:
        alive.data()
        imu.data()
        time.sleep(1)

# End of File
