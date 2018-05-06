'''
mainGUI.py

Created by Noopur Khachane
March 11, 2018
'''

from GUI import *
import cosmos
from cosmos import *
#from threading import Thread

Builder.load_file('kv_files/mainGUI2.kv')

class mainScreenMgr(ScreenManager):
    pass

class Presstransducers(BoxLayout):
    pressscreen = [None]*cosmos.vulcan2.NUM_PRESS

    def __init__(self, **kwargs):
        super(Presstransducers, self).__init__(**kwargs)
        self.orientation = 'vertical'
        cosmos.vulcan2.getPress()
        for i in range(len(self.pressscreen)):
            self.pressscreen[i] = Label(text = str(cosmos.vulcan2.presstransducers[i]),\
                                         font_size = self.height, \
                                         size_hint = (1.0, 0.1), \
                                         halign = 'right', \
                                         valign = 'middle')
            self.add_widget(self.pressscreen[i])

    def updatePress(self, dt):
        cosmos.vulcan2.getPress()
        for i in range(len(self.pressscreen)):
            self.pressscreen[i].text = str(cosmos.vulcan2.presstransducers[i])


class Thermocouples(BoxLayout):
    thermoscreen = [None]*cosmos.vulcan2.NUM_THERMO

    def __init__(self, **kwargs):
        super(Thermocouples, self).__init__(**kwargs)
        self.orientation = 'vertical'

        cosmos.vulcan2.getThermo()
        for i in range(len(self.thermoscreen)):
            self.thermoscreen[i] = Label(text = str(cosmos.vulcan2.thermocouples[i]),\
                                         font_size = self.height, \
                                         size_hint = (1.0, 0.1), \
                                         halign = 'right', \
                                         valign = 'middle')
            self.add_widget(self.thermoscreen[i])

    def updateThermo(self, dt):
        cosmos.vulcan2.getThermo()
        for i in range(len(self.thermoscreen)):
            self.thermoscreen[i].text = str(cosmos.vulcan2.thermocouples[i])

class StatusScreen(Screen):
    thermoscreen = [None]*cosmos.vulcan2.NUM_THERMO

    def __init__(self, **kwargs):
        super(StatusScreen, self).__init__(**kwargs)

        with self.canvas:
            self.rect = Rectangle(source = 'img/space.jpeg', size=self.size)
        self.bind(size=self.update_rect)

        box  = BoxLayout()
        box1 = Thermocouples()
        box2 = Presstransducers()

        box.add_widget(box1)
        box.add_widget(box2)
        self.add_widget(box)

        refresh_time = 0.1
        Clock.schedule_interval(box1.updateThermo, refresh_time)
        Clock.schedule_interval(box2.updatePress, refresh_time)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class GroundStationApp(App):

    def build(self):
        # Window.borderless = True
        # return a Button() as a root widget
        Window.borderless = True
        sm = mainScreenMgr()
        sm.add_widget(StatusScreen(name = "statusscreen"))
        return sm
