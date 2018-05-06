'''
vulcan2.py

Vulcan2

Created by Noopur Khachane
April 7, 2018
'''

from cosmos import *
from interface import *

class Vulcan2(Interface):
    """
    ###################################
    # Telemetry Items :               #
    #                                 #
    # 4 Thermocouple Readings         #
    # 3 Pressure Readings             #
    #                                 #
    ###################################
    # Command Items :                 #
    #                                 #
    # 1 Launch bit                    #
    #                                 #
    ###################################
    """
    NUM_THERMO = 4
    NUM_PRESS  = 3
    thermocouples    = [None]*NUM_THERMO
    presstransducers = [None]*NUM_PRESS

    def __init__(self):
        super().__init__("VULCAN2INT", "VULCAN2", "/dev")

    def getThermo(self):
        for i in range(len(self.thermocouples)):
            self.thermocouples[i] = self.getThermoRead(i+1)

    def getPress(self):
        for i in range(len(self.presstransducers)):
            self.presstransducers[i] = self.getPressRead(i+1)

    def getThermoRead(self, num):
        return tlm('VULCAN2 THERMOCOUPLES THERMO' + str(num))

    def getPressRead(self, num):
        return tlm('VULCAN2 PRESS_TRANSDUCERS PRESS' + str(num))
