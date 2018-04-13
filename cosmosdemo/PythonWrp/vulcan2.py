'''
vulcan2.py

Created by Noopur Khachane
April 7, 2018
'''

from cosmos import *

def getThermoRead(int num):
    return tlm('VULCAN2 THERMOCOUPLES THERMO' + str(num))

def getPressRead(int num):
    return tlm('VULCAN2 PRESS_TRANSDUCERS PRESS' + str(num))
