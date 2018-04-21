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

def startCosmos():
    os.system("ruby ../Launcher &")

def cntCosmos():
    while True:
        try:
            tlm('INST HEALTH_STATUS TEMP1')
        except:
            continue
        else:
            break
    print("Cosmos Server is Connected!")

def writePort(port, target, baudrate):
    fname = '../config/targets/' + target + '/cmd_tlm_server.txt'
    f = open(fname, 'w')
    server_config = makeStrings(port, target, baudrate)
    for string in server_config:
        f.write(string)
    f.close()

def makeStrings(port, target, baudrate):
    string1 = "INTERFACE " + target + " serial_interface.rb " + port + " " + \
        port + " " + baudrate + " NONE 1 10.0 nil LENGTH 0 8 0 1\n"
    string2 = "  TARGET " + target
    return [string1, string2]
