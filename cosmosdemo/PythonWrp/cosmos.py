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

def connect():
	os.system("ruby ../tools/CmdTlmServer &")
	while True:
		try:
			tlm('INST HEALTH_STATUS TEMP1')
		except:
			continue
		else:
			break

	print("Cosmos Server is Connected!")
