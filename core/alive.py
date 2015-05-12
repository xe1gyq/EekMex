#!/usr/bin/python

import logging

from system import System

def alive():

    system = System()
    cpu = system.cpu()
    memory = system.memory()
    message = "Cpu %s / Memory %s" % (cpu, memory)
    logging.info(message)

# End of File
