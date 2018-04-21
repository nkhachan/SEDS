'''
vulcan2.py

Created by Noopur Khachane
April 7, 2018
'''

#from cosmos import *
from interface import *

class Vulcan2(Interface):

    def __init__(self):
        super().__init__("VULCAN2INT", "VULCAN2", "/dev")

    def getThermoRead(self, num):
        return tlm('VULCAN2 THERMOCOUPLES THERMO' + str(num))

    def getPressRead(self, num):
        return tlm('VULCAN2 PRESS_TRANSDUCERS PRESS' + str(num))
