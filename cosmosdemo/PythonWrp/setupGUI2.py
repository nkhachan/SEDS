from GUI import *

Builder.load_file('kv_files/screens2.kv')

class ScreenMgr(ScreenManager):
    pass

class MainScreen(Screen):
    def gotoPortScreen(self, instance):
        instance.current = 'portscreen'

class PortScreen(Screen):
    pass

class Vulcan2Screen(Screen):
    pass

class SetUpApp(App):

    def build(self):
        sm = ScreenMgr()
        sm.add_widget(MainScreen(name = "Welcome Screen"))
        sm.add_widget(PortScreen(name = "Ports Screen"))
        #sm.add_widget(Vulcan2Screen(name = "Vulcan2 Screen"))
        return sm