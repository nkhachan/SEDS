'''
pressTable.py

Created by Noopur Khachane
April 7, 2018

Telemetry Items :

    Thermocouples
      Helium Ambient Temperature
      Electronics Panel Ambient Temperature

    Pressure Transducers
      K bottle Pressure
      RP1 Tank Pilot
      LOX Tank Pilot
      Helium Tank Fill
      PNA Pressure
      Extra One

Command Items :

    Actuation Board
      PNA1
      PNA2
      RP1 Tank Pilot
      LOX Tank Pilot
      Helium Tank Fill
      Electric Ball Valve 1
      Electric Ball Valve 2

'''
from cosmos import *
from interface import *

class PressTable(Interface):
    pThread = None
    sendable = False
    NUM_DRIVERS   = 6
    NUM_REGULATOR = 3
    # Output
    drivers     = [None]*NUM_DRIVERS
    # Input
    regulators  = [None]*NUM_REGULATOR

    def __init__(self):
        super().__init__("PRESSINT", "PRESSTABLE", "/dev")

    def setDriver(self, num, val):
        self.drivers[num] = val;

    def writeDrivers(self):
        print ("Sent Driver Reading")
        if (self.sendable):
            cmdString = "PRESSTABLE DRIVERS with "
            for i in range(len(self.drivers)):
                cmdString += "DRIVER" + str(i+1) + " " + str(self.drivers[i]) + ", "
            cmdString += "INIT 1"
            cmd(cmdString)

    def update(self):
        self.writeDrivers()
        self.pThread = threading.Timer(1.0, self.update).start()
