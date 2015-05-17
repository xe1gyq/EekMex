#!/usr/bin/python

import logging
import getopt
import math
import RTIMU
import sys
import time

class Imu(object):

    def __init__(self):

        self.imuSettingsFilePath = "/home/root/eekmex/configuration/imu.ini"
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
        logging.debug('Recommended Poll Interval: %dmS' % self.poll_interval)

    def data(self):

        while True:
            if self.imu.IMURead():
                # x, y, z = self.imu.getFusionData()
                # print("%f %f %f" % (x,y,z))
                data = self.imu.getIMUData()
                fusionPose = data["fusionPose"]
                logging.debug('Roll %f | Pitch %f | Yaw %f' %
                    (math.degrees(fusionPose[0]),
                    math.degrees(fusionPose[1]),
                    math.degrees(fusionPose[2])))
                time.sleep(self.poll_interval*1.0/1000.0)

# End of File
