'''
pressTable.py

Created by Noopur Khachane
April 7, 2018
'''

from cosmos import *
from interface import *

class PressTable(Interface):
    """
    ###################################
    # Telemetry Items :               #
    #                                 #
    #                                 #
    ###################################
    # Command Items :                 #
    #                                 #
    # 6 Bits for Driver Circuits      #
    # 3 Pressure value                #
    #                                 #
    ###################################
    """
    NUM_DRIVERS   = 6
    NUM_REGULATOR = 3
    drivers     = [None]*NUM_DRIVERS
    regulators  = [None]*NUM_REGULATOR

    def __init__(self):
        super().__init__("PRESSINT", "PRESSTABLE", "/dev")

    def sendDriverVal(self, num, val):
        cmd('PRESSTABLE DRIVERS DRIVER' + str(num))
