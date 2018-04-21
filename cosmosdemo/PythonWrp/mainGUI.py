'''
mainGUI.py

Created by Noopur Khachane
March 11, 2018
'''

from GUI import *
from threading import Thread

def get_microphone_level():
    """
    source: http://stackoverflow.com/questions/26478315/getting-volume-levels-from-pyaudio-for-use-in-arduino
    audioop.max alternative to audioop.rms
    """
    global levels
    while True:
        mx = 100
        if len(levels) >= 100:
            levels.pop()
        levels.append(mx)

class Logic(BoxLayout):

    def __init__(self,):
        super(Logic, self).__init__()
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 0.001)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j/5) for i, j in enumerate(levels)]

class GroundStationApp(App):
    def build(self):
        # Window.borderless = True
        # return a Button() as a root widget
        return Builder.load_file("kv_files/mainGUI.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    get_level_thread = Thread(target = get_microphone_level)
    get_level_thread.daemon = True
    get_level_thread.start()
    GroundStationApp().run()
