'''
setupGUI2.py

Created by Noopur Khachane
April 7, 2018
'''

from GUI import *
from cosmos import *
import cosmos
from usb import *

Builder.load_file('kv_files/screens2.kv')
Builder.load_file('kv_files/portscreen.kv')

class ScreenMgr(ScreenManager):
    pass

class MainScreen(Screen):

    def gotoPortScreen(self, instance):
        instance.current = 'portscreen'

class PortScreen(Screen):
    def on_enter(self):
        pass

    def writeVulcan2Port(self):
        cosmos.vulcan2.setPort('/dev')
        cosmos.vulcan2.writePort()

    def writePressTablePort(self):
        pass

    def exit(self):
        App.get_running_app().stop()

class PortDropDown(DropDown):
    pass


class SetUpApp(App):

    def build(self):
        Window.borderless = True
        sm = ScreenMgr()
        sm.add_widget(MainScreen(name = "mainscreen"))
        sm.add_widget(PortScreen(name = "portscreen"))
        return sm
