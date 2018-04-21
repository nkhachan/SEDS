'''
pressTable.py

Created by Noopur Khachane
April 7, 2018
'''

from cosmos import *
from interface import *

class PressTable(Interface):

    def __init__(self):
        super().__init__("PRESSINT", "PRESS", "/dev")
