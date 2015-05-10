#!/usr/bin/python

import argparse
import logging

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='EekMex, Amateur Radio Satellite Learning Platform')
    args = parser.parse_args()

    logging.basicConfig(filename='/home/root/eekmex/eekmex.log',level=logging.DEBUG)
    logging.info('EekMex Logging')

    while True:
        pass

# End of File
