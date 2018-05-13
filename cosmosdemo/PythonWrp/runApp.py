'''
runApp

Created by Noopur Khachane
April 7, 2018
'''

from cosmos import *
from mainGUI import *
from setupGUI2 import *
import sys


def main():
    #SetUpApp().run()
    cosmos.connect()
    GroundStationApp().run()

if __name__ == "__main__":
    main()
