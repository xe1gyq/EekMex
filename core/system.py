import commands
import logging
import numpy
import math
import psutil

from utilities import BytesToHuman

class System(object):

    def __init__(self):
        pass

    def cpu(mode):
        output = psutil.cpu_times_percent(interval=1, percpu=False)
        return "%.1f" % output.system

    def memory(self):
        output = psutil.virtual_memory()
        return BytesToHuman(output.total)

# End of File
