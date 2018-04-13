'''
setupGUI2.py

Created by Noopur Khachane
April 7, 2018
'''

from GUI import *
from cosmos import *

Builder.load_file('kv_files/screens2.kv')
Builder.load_file('kv_files/portscreen.kv')

class ScreenMgr(ScreenManager):
    pass

class MainScreen(Screen):

    def gotoPortScreen(self, instance):
        instance.current = 'portscreen'

class PortScreen(Screen):

    def writeVulcan2Port(self):
        writePort('/dev','VULCAN2', '57600')

    def writePressTablePort(self):
        writePort('/dev','PRESSTABLE', '57600')

class Vulcan2Screen(Screen):
    pass

class SetUpApp(App):

    def build(self):
        sm = ScreenMgr()
        sm.add_widget(MainScreen(name = "Welcome Screen"))
        sm.add_widget(PortScreen(name = "Ports Screen"))
        #sm.add_widget(Vulcan2Screen(name = "Vulcan2 Screen"))
        return sm
