from vulcan2 import *
from pressTable import *
from StateManager import *
import cosmos
from cosmos import *
import threading
import time

class GroundStation:
    #__instance = None
    # Create instances of our interfaces
    vulcan2    = Vulcan2()
    presstable = PressTable()

    # State of the GSC
    mgr = StateManager()

    # Make a singleton later
    '''def getInstance():
        """ Static access method """
        if GroundStation.__instance == None:
            GroundStation()
        return GroundStation.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton")
        else:
            Singleton.__instance = self
            self.update()'''

    def start(self):
        # Start the COSMOS telemetry server
        cosmos.connect()
        # Start threads for Vulcan2 and Pressure Table Data Acquisition, and
        # state manager checks
        try :
            self.vulcan2.vThread = threading.Thread(name = 'vulcan2', target = self.vulcan2.update())
            self.vulcan2.vThread.start()

            self.presstable.pThread = threading.Thread(name = 'pressTable', target = self.presstable.update())
            self.presstable.pThread.start()

            self.mgr.sThread = threading.Thread(name = 'state', target = self.mgr.run())
            self.mgr.sTrhead.start()
        except :
            print ("Threading Failure")
