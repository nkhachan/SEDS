import sys
sys.path.append("/home/noopur/python-ballcosmos")
import os
os.environ["COSMOS_USERPATH"] = "/home/noopur/cosmosdemo"
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
