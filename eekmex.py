#!/usr/bin/python

import argparse
import logging

def eekMexLogging():

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        #datefmt='%m-%d %H:%M',
                        filename='/home/root/eekmex/eekmex.log',
                        filemode='w')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logging.info('EekMex Logging')

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='EekMex, Amateur Radio Satellite Learning Platform')
    args = parser.parse_args()

    eekMexLogging()
    while True:
        pass

# End of File
