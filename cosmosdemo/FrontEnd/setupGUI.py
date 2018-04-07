'''
GUI for Ground Station

Created by Noopur Khachane
March 11, 2018
'''
from GUI import *

Builder.load_file('kv_files/screens.kv')

def getPorts():
    return ["banana", "apple"]

class PortScreen(Screen):
    pass

class Vulcan2Screen(Screen):
    pass

class PressureTableScreen(Screen):
    pass

screen_manager = ScreenManager()

screen_manager.add_widget(PortScreen(name="screen_one"))
screen_manager.add_widget(Vulcan2Screen(name="screen_two"))
screen_manager.add_widget(PressureTableScreen(name="screen_three"))

class SetUpApp(App):
    def build(self):
        # return a Button() as a root widget
        return screen_manager
