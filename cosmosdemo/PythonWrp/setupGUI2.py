'''
setupGUI2.py

Created by Noopur Khachane
April 7, 2018
'''

from GUI import *
from cosmos import *
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
        writePort('/dev','VULCAN2', '57600')

    def writePressTablePort(self):
        writePort('/dev','PRESSTABLE', '57600')

    def exit(self):
        App.get_running_app().stop()
class Vulcan2Screen(Screen):
    pass

class PortDropDown(DropDown):
    pass


class SetUpApp(App):

    def build(self):
        Window.borderless = True
        sm = ScreenMgr()
        sm.add_widget(MainScreen(name = "mainscreen"))
        sm.add_widget(PortScreen(name = "portscreen"))
        #sm.add_widget(Vulcan2Screen(name = "Vulcan2 Screen"))
        return sm
