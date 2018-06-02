'''
mainGUI.py

Created by Noopur Khachane
March 11, 2018
'''

from GUI import *
from Vulcan2Gui import *
from PressTableGui import *

class mainScreenMgr(ScreenManager):
    pass

class StatusBox(BoxLayout):
    def __init__(self, GS, **kwargs):
        super(StatusBox, self).__init__(**kwargs)
        self.orientation = 'vertical'

        box1 = Vulcan2Box(GS)
        box2 = PressTableBox(GS)

        self.add_widget(box1)
        self.add_widget(box2)

class StatusScreen(Screen):

    def __init__(self, GS, **kwargs):
        super(StatusScreen, self).__init__(**kwargs)

        with self.canvas:
            self.rect = Rectangle(source = 'img/space.jpeg', size=self.size)
        self.bind(size=self.update_rect)

        box1 = StatusBox(GS)
        self.add_widget(box1)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class GroundStationApp(App):

    def setGS(self, GS):
        self.GS = GS

    def build(self):
        Window.borderless = True
        sm = mainScreenMgr()
        sm.add_widget(StatusScreen(self.GS, name = "statusscreen"))
        return sm
