from enum import Enum

class state(Enum):
    IDLE    = 0
    LIVE    = 1
    CONFIG  = 2
    FILL    = 3
    READY   = 4
    LAUNCH  = 5
    ABORT   = 6
    WARNING = 7

class StateManager():
    # Thread for updates from COSMOS server
    sThread = None
    current = state.IDLE

    def _init_(self):
        pass

    def run(self):
        pass
