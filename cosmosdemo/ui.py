'''
GUI for Ground Station

Created by Noopur Khachane
March 11, 2018
'''

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button


class GroundStationApp(App):

    def build(self):
        # return a Button() as a root widget
        return Button(text='hello world')

if __name__ == '__main__':
    GroundStationApp().run()
