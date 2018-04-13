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

def writePort(portname, target, baudrate):
    fname = '../config/targets/' + target + '/cmd_tlm_server.txt'
    print ("In cosmos function " + target)
    f = open(fname, 'r')
    config = f.readline()
    f.close()
    tokens = config.split(' ')
    tokens[3] = portname
    tokens[4] = portname
    tokens[5] = baudrate
    print (" ".join(tokens))
