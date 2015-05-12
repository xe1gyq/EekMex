#!/usr/bin/python

import logging

from system import System

class Alive(object):

    def __init__(self):

        self.system = System()
        logging.info('Alive Initialization Succeeded!')

    def data(self):

        cpu = self.system.cpu()
        memory = self.system.memory()
        message = "Cpu %s / Memory %s" % (cpu, memory)
        logging.info(message)

# End of File
