'''
vulcan2.py

Vulcan2

Created by Noopur Khachane
April 7, 2018

Telemetry Items :

    Voltage/Current Measurements
      0 - Main Battery Voltage
      1 - Main Battery Current
      3 - 5V Rail
      4 - 5V Rail Current
      5 - 24V Rail
      6 - 24V Rail Current

    4 Thermocouple Readings
      0 - LOX Tank
      1 - Helium Tank
      2 - RP1 Tank

    5 Pressure Readings
      0 - LOX Tank
      1 - Helium Tank
      2 - RP1 Tank
      3 - RP1 Tank Pilot
      4 - LOX Tank Pilot

    Actuation Board
      3 Recovery E-matches (Read Only)

Command Items :

    Actuation Board
      0 - LOX Vent Valve
      1 - RP1 Vent Valve
      2 - Ignition E-matches

'''

from cosmos import *
from interface import *

class Vulcan2(Interface):
    # Thread for updates from COSMOS server
    vThread    = None

    # TELEMETRY ITEMS
    # Thermocouple Readings
    NUM_THERMO    = 3
    thermocouples = [None]*NUM_THERMO
    thermonames   = ["LOX Tank", "Helium Tank", "RP1 Tank"]

    # Pressure Trnsducer Readings
    NUM_PRESS        = 5
    presstransducers = [None]*NUM_PRESS
    pressnames       = ["LOX Tank", "Helium Tank", "RP1 Tank", "RP1 Tank Pilot", \
                        "LOX Tank Pilot"]
    # Ematch state (Read only)
    NUM_ACT_REC      = 3
    actuationrec     = [None]*NUM_ACT_REC

    # Battery Readings
    NUM_BATTERY   = 6
    batteries     = [None]*NUM_BATTERY
    battnames     = ["Main Battery Voltage", "Main Battery Current", "5V Rail", \
                     "5V Rail Current", "24V Rail", "24 Rail Current"]

    # COMMAND ITEMS
    # Actuation Board Output
    NUM_ACTUATION    = 3
    actuationsend    = [None]*NUM_ACTUATION


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
        # Run thread again
        self.vThread = threading.Timer(1.0, self.update).start()
