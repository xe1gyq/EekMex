#!/usr/bin/python

import argparse
import logging
import threading
import time

from core.alive import Alive
from core.imu import Imu
from core.bpta import Bpta

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

    alive = Alive()
    bpta = Bpta()
    imu = Imu()

    threadbpta = threading.Thread(name='bpta', target=bpta.data)
    threadimu = threading.Thread(name='imu', target=imu.data)

    threadbpta.start()
    threadimu.start()

    while True:
        alive.data()
        time.sleep(1)

# End of File
