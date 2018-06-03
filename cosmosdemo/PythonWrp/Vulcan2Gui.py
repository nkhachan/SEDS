from GUI import *


class Vulcan2Box(BoxLayout):
    def __init__(self, GS, **kwargs):
        super(Vulcan2Box, self).__init__(**kwargs)
        self.orientation = 'vertical'

        box1 = Thermocouples(GS)
        box2 = Presstransducers(GS)
        box3 = ThermoPlot(GS)

        self.add_widget(box3)
        self.add_widget(box1)
        self.add_widget(box2)

        refresh_time = 0.1
        Clock.schedule_interval(box1.updateThermo, refresh_time)
        Clock.schedule_interval(box2.updatePress,  refresh_time)
        Clock.schedule_interval(box3.updateGraph,  refresh_time)

class ThermoPlot(BoxLayout):
    Y      = None
    graphs = None
    GS     = None

    def __init__(self, GS,**kwargs):
        super(ThermoPlot, self).__init__(**kwargs)
        self.GS     = GS
        self.Y      = [None]*self.GS.vulcan2.NUM_THERMO
        self.graphs = [None]*self.GS.vulcan2.NUM_THERMO

        plt.ion()

        for i in range(self.GS.vulcan2.NUM_THERMO):
            self.Y[i] = [0]*GRAPH_RANGE
            self.graphs[i] = plt.plot(self.Y[:][i], label = str(i))[0]

        plt.ylim((0, 1400))
        plt.ylabel('Thermocouples')
        plt.legend()

        thermoplt = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(thermoplt)

    def updateGraph(self,dt):
        for i in range(self.GS.vulcan2.NUM_THERMO):
            self.Y[:][i].pop(0)
        for i in range(self.GS.vulcan2.NUM_THERMO):
            self.Y[:][i].append(self.GS.vulcan2.thermocouples[i])
        for i in range(self.GS.vulcan2.NUM_THERMO):
            self.graphs[i].set_ydata(self.Y[:][i])
        plt.draw()

class Thermocouples(BoxLayout):
    thermoscreen = None
    GS           = None

    def __init__(self, GS, **kwargs):
        super(Thermocouples, self).__init__(**kwargs)
        self.thermoscreen = [None]*GS.vulcan2.NUM_THERMO
        self.orientation  = 'vertical'
        self.height       = 100
        self.size_hint_y  = 1
        self.GS           = GS

        title = Label(text      = "Thermocouples", \
                      font_size = self.height*0.5)
        self.add_widget(title)
        
        for i in range(len(self.thermoscreen)):
            self.thermoscreen[i] = Label(text = str(self.GS.vulcan2.thermocouples[i]),\
                                         font_size = self.height)
            self.add_widget(self.thermoscreen[i])

    def updateThermo(self, dt):
        for i in range(len(self.thermoscreen)):
            self.thermoscreen[i].text = str(self.GS.vulcan2.thermocouples[i])


class Presstransducers(BoxLayout):
    pressscreen = None
    GS          = None

    def __init__(self, GS, **kwargs):
        super(Presstransducers, self).__init__(**kwargs)
        self.GS = GS
        self.pressscreen = [None]*self.GS.vulcan2.NUM_PRESS
        self.orientation = 'vertical'
        self.height      = 100
        self.size_hint_y = 1

        title = Label(text      = "Pressure\n Transducers", \
                      font_size = self.height*0.5, \
                      halign    = 'center')

        self.add_widget(title)
        for i in range(len(self.pressscreen)):
            self.pressscreen[i] = Label(text = str(self.GS.vulcan2.presstransducers[i]),\
                                         font_size = self.height)
            self.add_widget(self.pressscreen[i])

    def updatePress(self, dt):
        for i in range(len(self.pressscreen)):
            self.pressscreen[i].text = str(self.GS.vulcan2.presstransducers[i])

if __name__ == '__main__':
    Vulcan2App(GS).run()
