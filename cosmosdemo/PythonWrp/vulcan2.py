'''
vulcan2.py

Vulcan2

Created by Noopur Khachane
April 7, 2018

Telemetry Items :

    Voltage/Current Measurements
      Main Battery Voltage
      Main Battery Current
      5V Rail
      5V Rail Current
      24V Rail
      24V Rail Current

    4 Thermocouple Readings
      LOX Tank
      Helium Tank
      RP1 Tank

    5 Pressure Readings
      LOX Tank
      Helium Tank
      RP1 Tank
      RP1 Tank Pilot
      LOX Tank Pilot

    Actuation Board
      3 Recovery E-matches (Read Only)

Command Items :

    Actuation Board
      LOX Vent Valve
      RP1 Vent Valve
      Ignition E-matches

'''

from cosmos import *
from interface import *

class Vulcan2(Interface):
    vThread    = None
    NUM_THERMO = 4
    NUM_PRESS  = 3
    thermocouples    = [None]*NUM_THERMO
    presstransducers = [None]*NUM_PRESS

    def __init__(self):
        super().__init__("VULCAN2INT", "VULCAN2", "/dev")

    def getThermo(self):
        print ("Got Thermocouple Reading")
        for i in range(len(self.thermocouples)):
            self.thermocouples[i] = self.getThermoRead(i+1)

    def getPress(self):
        print ("Got Transducer Reading")
        for i in range(len(self.presstransducers)):
            self.presstransducers[i] = self.getPressRead(i+1)

    def getThermoRead(self, num):
        return tlm('VULCAN2 THERMOCOUPLES THERMO' + str(num))

    def getPressRead(self, num):
        return tlm('VULCAN2 PRESS_TRANSDUCERS PRESS' + str(num))

    def update(self):
        self.getThermo()
        self.getPress()
        self.vThread = threading.Timer(1.0, self.update).start()
