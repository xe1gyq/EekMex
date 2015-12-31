#! /usr/bin/python

import logging
import math
from random import randint
from time import *
import time
import threading
from threading import Thread
try:
    import RTIMU
except ImportError:
    pass

class emImu(object):

    def __init__(self, mode=None):

        logging.info('Inertial Measurement Unit')
        self.mode = mode
        self.roll = None
        self.pitch = None
        self.yaw = None

        if mode is None:
            self.emImuInitialize()

        thread = Thread(target=self.emImuPoller)
        thread.start()

    def emImuInitialize(self):
        self.imuSettingsFilePath = "/home/root/eekmex/configuration/emimu.ini"
        self.imuSettingsFileDescriptor = RTIMU.Settings(self.imuSettingsFilePath)

        self.imu = RTIMU.RTIMU(self.imuSettingsFileDescriptor)

        logging.info('IMU ' + self.imu.IMUName())

        if (not self.imu.IMUInit()):
            logging.error('IMU Initialization Failed!')
            sys.exit(1)
        else:
            logging.info('IMU Initialization Succeeded!')

        self.imu.setSlerpPower(0.02)
        self.imu.setGyroEnable(True)
        self.imu.setAccelEnable(True)
        self.imu.setCompassEnable(True)
        self.poll_interval = self.imu.IMUGetPollInterval()

    def emImuPoller(self):
        while True:
            if self.mode is None: 
                if self.imu.IMURead():
                    data = self.imu.getIMUData()
                    fusionPose = data["fusionPose"]
                    self.roll = math.degrees(fusionPose[0])
                    self.pitch = math.degrees(fusionPose[1])
                    self.yaw = math.degrees(fusionPose[2])
                    time.sleep(self.poll_interval*1.0/1000.0)
            else:
                self.roll = randint(0,340)
                self.pitch = randint(-180,180)
                self.yaw = randint(-180,180)

    def emImuData(self):
        imudata = ("Imu: {0}," "{1}," "{2},".format(self.roll, self.pitch, self.yaw))
        logging.info(imudata)
        return self.roll, self.pitch, self.yaw

    def emImuRoll(self):
        return self.roll

    def emImuPitch(self):
        return self.pitch

    def emImuYaw(self):
        return self.yaw

# End of File
