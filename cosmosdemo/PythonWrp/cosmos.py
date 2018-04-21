'''
cosmos.py

Created by Noopur Khachane
April 7, 2018
'''


cosmos_names = {
		"VULCAN2" : "VULCAN2INT",
		"PRESSTABLE" : "PRESSINT",
	}

import sys
sys.path.append("python-ballcosmos")

import os
os.environ["COSMOS_USERPATH"] = "cosmosdemo"

from ballcosmos.script import *

class Cosmos(object):

	def connect(self):
		os.system("ruby ../Launcher &")
		while True:
			try:
				tlm('INST HEALTH_STATUS TEMP1')
			except:
				continue
			else:
				break
		print("Cosmos Server is Connected!")


	def initialize_Interfaces(self):
		vulcan2int = 
