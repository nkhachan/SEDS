import cosmos
from cosmos import *
from GUI import *

class PressTableBox(BoxLayout):
    def __init__(self, **kwargs):
        super(PressTableBox, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = 0.5

        box1 = Drivers()
        box2 = Regulators()

        self.add_widget(box1)
        self.add_widget(box2)

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
            self.driversscreen[i] = Switch()
            self.add_widget(Label(text = str(i+1), font_size = self.height*0.4))
            self.add_widget(self.driversscreen[i])

        setDrivers = Button(text = "Write Drivers", \
                            font_size = self.height*0.2)
        setDrivers.bind(on_press = self.writeDrivers)
        self.add_widget(setDrivers)

    def writeDrivers(self,instance):
        #pass
        for i in range(len(self.driversscreen)):
            cosmos.presstable.setDriver(i, self.driversscreen[i].active*1)
        cosmos.presstable.writeDrivers()
