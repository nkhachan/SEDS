'''
GUI.py

Created by Noopur Khachane
April 7, 2018
'''

import os
#os.environ["KIVY_NO_FILELOG"] = "1"
#os.environ["KIVY_NO_CONSOLELOG"] = "1"

import kivy
kivy.require('1.0.7')

from kivy.config import Config
Config.set('graphics', 'width', '2000')
Config.set('graphics', 'height', '100')

import matplotlib.pyplot as plt
import random
import numpy as np
import multiprocessing
import threading
from threading import *

plt.style.use('dark_background')
GRAPH_RANGE = 75

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.graphics import Rectangle
from kivy.uix.switch import Switch
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (3000, 1000)
