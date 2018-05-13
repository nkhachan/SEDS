
class GroundStation:
    __instance = None

    def getInstance():
        """ Static access method """
        if GroundStation.__instance == None:
            GroundStation()
        return
