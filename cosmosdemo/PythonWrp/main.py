from GroundStation import *
from setupGUI import *
from mainGUI import *
import multiprocessing

def main():
    # Run Configuration Applications
    #SetUpApp().run()

    # Start Ground Station (aka Communication with Cosmos Server)
    GS = GroundStation()
    #GS.start()

    # Start Main Ground Station Application
    GSApp = GroundStationApp(GS)
    GSApp.run()

if __name__ == "__main__":
    main()
