import cosmos
from cosmos import *
from GUI import *

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


class ThermoPlot(BoxLayout):
    Y = [None]*cosmos.vulcan2.NUM_THERMO
    graphs = [None]*cosmos.vulcan2.NUM_THERMO
    plt.ion()
    for i in range(cosmos.vulcan2.NUM_THERMO):
        Y[i] = [0]*GRAPH_RANGE
        graphs[i] = plt.plot(Y[:][i], label = str(i))[0]

    def __init__(self, **kwargs):
        super(ThermoPlot, self).__init__(**kwargs)
        plt.ylim((0, 1400))
        plt.ylabel('Thermocouples')
        plt.legend()

        thermoplt = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(thermoplt)

    def updateGraph(self,dt):
        for i in range(cosmos.vulcan2.NUM_THERMO):
            self.Y[:][i].pop(0)
        for i in range(cosmos.vulcan2.NUM_THERMO):
            self.Y[:][i].append(cosmos.vulcan2.getThermoRead(i+1))
        for i in range(cosmos.vulcan2.NUM_THERMO):
            self.graphs[i].set_ydata(self.Y[:][i])
        plt.draw()

class Thermocouples(BoxLayout):
    thermoscreen = [None]*cosmos.vulcan2.NUM_THERMO

    def __init__(self, **kwargs):
        super(Thermocouples, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.height = 100
        self.size_hint_y = 1

        cosmos.vulcan2.getThermo()
        title = Label(text = "Thermocouples", \
                      font_size = self.height*0.5)
        self.add_widget(title)
        for i in range(len(self.thermoscreen)):
            self.thermoscreen[i] = Label(text = str(cosmos.vulcan2.thermocouples[i]),\
            #self.thermoscreen[i] = Label(text = '0',\
                                         font_size = self.height)
            self.add_widget(self.thermoscreen[i])

    def updateThermo(self, dt):
        cosmos.vulcan2.getThermo()
        for i in range(len(self.thermoscreen)):
            self.thermoscreen[i].text = str(cosmos.vulcan2.thermocouples[i])


class Presstransducers(BoxLayout):
    pressscreen = [None]*cosmos.vulcan2.NUM_PRESS

    def __init__(self, **kwargs):
        super(Presstransducers, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.height = 100
        self.size_hint_y = 1

        cosmos.vulcan2.getPress()
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
        cosmos.vulcan2.getPress()
        for i in range(len(self.pressscreen)):
            self.pressscreen[i].text = str(cosmos.vulcan2.presstransducers[i])
