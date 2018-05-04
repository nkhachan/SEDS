'''
setupGUI.py

Created by Noopur Khachane
April 7, 2018
'''

from GUI import *

#Builder.load_file('kv_files/screens.kv')

class PortScreen(Screen):
    pass

class Vulcan2Screen(Screen):
    pass

class PressureTableScreen(Screen):
    pass

class PortDropDown(DropDown):
    pass

#sm = ScreenManager()
#sm.add_widget(PortScreen(name="screen_one"))
#sm.add_widget(Vulcan2Screen(name="screen_two"))
#sm.add_widget(PressureTableScreen(name="screen_three"))

class SetUpApp(App):
    def build(self):
        return sm
