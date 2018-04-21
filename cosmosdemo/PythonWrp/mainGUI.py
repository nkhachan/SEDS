'''
mainGUI.py

Created by Noopur Khachane
March 11, 2018
'''

from GUI import *



class Vulcan2Tab(TabbedPanel):
    pass

class GroundStationApp(App):

    def build(self):
        Window.borderless = True
        # return a Button() as a root widget
        return Button(text='hello world')
