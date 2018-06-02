from GroundStation import *
from setupGUI2 import *
from mainGUI import *

def main():
    SetUpApp().run()
    GS = GroundStation()
    GS.start()
    GSApp = GroundStationApp()
    GSApp.setGS(GS)
    GSApp.run()

if __name__ == "__main__":
    #SetUpApp().run()
    #GS = GroundStation()
    main()
