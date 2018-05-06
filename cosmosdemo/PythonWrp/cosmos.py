'''
cosmos.py

Created by Noopur Khachane
April 7, 2018
'''

import sys
sys.path.append("python-ballcosmos")

import os
os.environ["COSMOS_USERPATH"] = "cosmosdemo"

from ballcosmos.script import *
from vulcan2 import *
from pressTable import *

# Create our 2 interfaces

vulcan2    = Vulcan2()
presstable = PressTable()


def connect():
	os.system("ruby ../Launcher &")
	while True:
		try:
			tlm('INST HEALTH_STATUS TEMP1')
		except:
			continue
		else:
			break

	print("Cosmos Server is Connected!")
