'''
mainGUI.py

Created by Noopur Khachane
March 11, 2018
'''

from GUI import *
import cosmos
from cosmos import *

class mainScreenMgr(ScreenManager):
    pass

class Presstransducers(BoxLayout):
    pressscreen = [None]*cosmos.vulcan2.NUM_PRESS

    def __init__(self, **kwargs):
        super(Presstransducers, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.height = 100
        self.size_hint_y = 1

        #cosmos.vulcan2.getPress()
        title = Label(text = "Pressure\n Transducers", \
                      font_size = self.height*0.5, \
                      halign = 'center')

        self.add_widget(title)
        for i in range(len(self.pressscreen)):
            self.pressscreen[i] = Label(text = str(cosmos.vulcan2.presstransducers[i]),\
            #self.pressscreen[i] = Label(text = '0',\
                                         font_size = self.height)
            self.add_widget(self.pressscreen[i])

    def updatePress(self, dt):
        #cosmos.vulcan2.getPress()
        for i in range(len(self.pressscreen)):
            self.pressscreen[i].text = str(cosmos.vulcan2.presstransducers[i])

class ThermoPlot(BoxLayout):
    Y = [0]*50
    Z = [0]*50
    plt.ion()
    graph = plt.plot(Y)[0]
    graph2 = plt.plot(Z)[0]

    def __init__(self, **kwargs):
        super(ThermoPlot, self).__init__(**kwargs)
        plt.ylim((0, 1023))
        plt.ylabel('Thermocouples')

        thermoplt = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(thermoplt)

    def updateGraph(self,dt):
        self.Y.pop(0)
        self.Z.pop(0)
        self.Y.append(cosmos.vulcan2.getThermoRead(1))
        self.Z.append(cosmos.vulcan2.getThermoRead(2))
        self.graph.set_ydata(self.Y)
        self.graph2.set_ydata(self.Z)
        plt.draw()


class Thermocouples(BoxLayout):
    thermoscreen = [None]*cosmos.vulcan2.NUM_THERMO

    def __init__(self, **kwargs):
        super(Thermocouples, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.height = 100
        self.size_hint_y = 1

        #cosmos.vulcan2.getThermo()
        title = Label(text = "Thermocouples", \
                      font_size = self.height*0.5)
        self.add_widget(title)
        for i in range(len(self.thermoscreen)):
            self.thermoscreen[i] = Label(text = str(cosmos.vulcan2.thermocouples[i]),\
            #self.thermoscreen[i] = Label(text = '0',\
                                         font_size = self.height)
            self.add_widget(self.thermoscreen[i])

    def updateThermo(self, dt):
        #cosmos.vulcan2.getThermo()
        for i in range(len(self.thermoscreen)):
            self.thermoscreen[i].text = str(cosmos.vulcan2.thermocouples[i])

class Regulators(BoxLayout):
    regulatorscreen = [None]*cosmos.presstable.NUM_REGULATOR

    def __init__(self, **kwargs):
        super(Regulators, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.height = 100
        self.size_hint_y = 1

        title = Label(text = "Pressure\n Regulators", \
                      font_size = self.height*0.5, \
                      halign = 'center')
        self.add_widget(title)

        for i in range(len(self.regulatorscreen)):
            #self.regulatorscreen[i] = Label(text = str(cosmos.presstable.thermocouples[i]),\
            self.regulatorscreen[i] = Label(text = '0',\
                                         font_size = self.height)
            self.add_widget(self.regulatorscreen[i])

class Drivers(BoxLayout):
    driversscreen = [None]*cosmos.presstable.NUM_DRIVERS

    def __init__(self, **kwargs):
        super(Drivers, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.height = 100
        self.size_hint_y = 1

        title = Label(text = "Drivers", \
                      font_size = self.height*0.5)

        self.add_widget(title)

        for i in range(len(self.driversscreen)):
            #self.regulatorscreen[i] = Label(text = str(cosmos.presstable.thermocouples[i]),\
            self.driversscreen[i] = Switch()
            self.add_widget(Label(text = str(i), font_size = self.height*0.4))
            self.add_widget(self.driversscreen[i])

        setDrivers = Button(text = "Write Drivers", \
                            font_size = self.height*0.2)
        setDrivers.bind(on_press = self.writeDrivers)
        self.add_widget(setDrivers)

    def writeDrivers(self,instance):
        pass
        #for i in range(len(self.driversscreen)):
        #    cosmos.presstable.setDriver(i, self.driversscreen[i].active*1)
        #cosmos.presstable.writeDrivers()

class Vulcan2Box(BoxLayout):
    def __init__(self, **kwargs):
        super(Vulcan2Box, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = 0.5

        box1 = Thermocouples()
        box2 = Presstransducers()
        box3 = ThermoPlot()

        self.add_widget(box1)
        self.add_widget(box2)
        self.add_widget(box3)

        refresh_time = 0.1
        Clock.schedule_interval(box1.updateThermo, refresh_time)
        Clock.schedule_interval(box2.updatePress, refresh_time)
        Clock.schedule_interval(box3.updateGraph, refresh_time)

class PressTableBox(BoxLayout):
    def __init__(self, **kwargs):
        super(PressTableBox, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = 0.5

        box1 = Drivers()
        box2 = Regulators()

        self.add_widget(box1)
        self.add_widget(box2)

class StatusBox(BoxLayout):
    def __init__(self, **kwargs):
        super(StatusBox, self).__init__(**kwargs)
        self.orientation = 'vertical'

        box1 = Vulcan2Box()
        box2 = PressTableBox()

        self.add_widget(box1)
        self.add_widget(box2)

class StatusScreen(Screen):

    def __init__(self, **kwargs):
        super(StatusScreen, self).__init__(**kwargs)

        with self.canvas:
            self.rect = Rectangle(source = 'img/space.jpeg', size=self.size)
        self.bind(size=self.update_rect)

        box1 = StatusBox()
        self.add_widget(box1)

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
