#!/usr/bin/python

import logging
import getopt
import math
import sys
import time

import RTIMU

class Imu(object):

    def __init__(self):

        imuSettingsFilePath = "/home/root/eekmex/configuration/imu.ini"
        imuSettingsFileDescriptor = RTIMU.Settings(imuSettingsFilePath)
        self.imu = RTIMU.RTIMU(imuSettingsFileDescriptor)

        logging.info('IMU Name ' + self.imu.IMUName())

        if (not self.imu.IMUInit()):
            sys.exit(1)

        self.imu.setSlerpPower(0.02)
        self.imu.setGyroEnable(True)
        self.imu.setAccelEnable(True)
        self.imu.setCompassEnable(True)

        self.poll_interval = self.imu.IMUGetPollInterval()

    def data(self):

        print 'Temp'
        if self.imu.IMURead():
            # x, y, z = self.imu.getFusionData()
            # print("%f %f %f" % (x,y,z))
            data = self.imu.getIMUData()
            fusionPose = data["fusionPose"]
            logging.info('Roll %f | Pitch %f | Yaw %f' % (math.degrees(fusionPose[0]), math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
            time.sleep(self.poll_interval*1.0/10.0)

# End of File
