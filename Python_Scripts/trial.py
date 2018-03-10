import sys
sys.path.append("/usr/local/lib/python3.5/dist-packages")

import os
os.environ["COSMOS_USERPATH"] = "/media/noopur/New Volume/SEDS/OpenSatKit-master/cosmos"

from ballcosmos.script import *

print("Hello")
print(tlm('INST HEALTH_STATUS TEMP1'))
