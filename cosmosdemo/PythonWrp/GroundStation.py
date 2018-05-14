
class GroundStation:
    __instance = None
    # Create instances of our interfaces
    vulcan2    = Vulcan2()
    presstable = PressTable()

    # State of the GSC
    mgr = StateManager(state.IDLE)

    def getInstance():
        """ Static access method """
        if GroundStation.__instance == None:
            GroundStation()
        return GroundStation.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton")
        else:
            Singleton.__instance = self

    def update():
        vulcan2.update()
        presstable.update()
