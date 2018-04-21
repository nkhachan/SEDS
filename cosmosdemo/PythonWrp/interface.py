class Interface:

    name = ""
    target = ""
    baudrate = 57600
    port = ""

    def _init_(self, someName, targetName, baudRate):
        name = someName
        target = targetName
        baudrate = baudRate

    def setName(self, someName):
        name = someName

    def setTarget(self, targetName):
        target = targetName

    def setBaudRate(self, baudRate):
        baudrate = baudRate

    def setPort(self, portName):
        port = portName

    def writePort(self):
        fname = '../config/targets/' + target + '/cmd_tlm_server.txt'
        f = open(fname, 'w')
        server_config = makeConfigStrings(port, target, baudrate)
        for string in server_config:
            f.write(string)
        f.close()

    def makeConfigStrings(self):
        string1 = "INTERFACE " + target + " serial_interface.rb " + port + " " + \
            port + " " + baudrate + " NONE 1 10.0 nil LENGTH 0 8 0 1\n"
        string2 = "  TARGET " + target
        return [string1, string2]
