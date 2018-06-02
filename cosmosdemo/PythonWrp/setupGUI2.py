'''
setupGUI2.py

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
Config.set('graphics', 'height', '1500')

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.core.window import Window

from cosmos import *
import cosmos
from usb import *

Builder.load_file('kv_files/screens2.kv')
Builder.load_file('kv_files/portscreen.kv')

class setupScreenMgr(ScreenManager):
    pass

class MainScreen(Screen):

    def gotoPortScreen(self, instance):
        instance.current = 'portscreen'

class PortScreen(Screen):

    def on_enter(self):
        pass

    def writeVulcan2Port(self, port):
        cosmos.vulcan2.setPort(port)
        cosmos.vulcan2.writePort()

    def writePressTablePort(self, port):
        cosmos.presstable.setPort(port)
        cosmos.presstable.writePort()

    def exit(self):
        App.get_running_app().stop()

class SetUpApp(App):

    def build(self):
        Window.borderless = True
        sm = setupScreenMgr()
        sm.add_widget(MainScreen(name = "mainscreen"))
        sm.add_widget(PortScreen(name = "portscreen"))
        return sm
