#! /usr/bin/python

import logging
import math
from time import *
import time
import threading
from threading import Thread
from random import randint

class emImu(object):

    def __init__(self):

        logging.info('Inertial Measurement Unit')
        self.roll = None
        self.pitch = None
        self.yaw = None

        self.emImuInitialize()
        thread = Thread(target=self.emImuPoller)
        thread.start()

    def emImuInitialize(self):
        logging.info('IMU ' + 'Simulator')
        logging.info('IMU Initialization Succeeded!')

    def emImuPoller(self):
        while True:
                self.roll = randint(0,180)
                self.pitch = randint(0,180)
                self.yaw = randint(0,180)

    def emImuRollGet(self):
        return self.roll

    def emImuPitchGet(self):
        return self.pitch

    def emImuYawGet(self):
        return self.yaw

# End of File
