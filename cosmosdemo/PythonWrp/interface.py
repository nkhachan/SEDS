'''
interface.py

Interface Base Class

Create by Noopur Khachane
April 21, 2018
'''

class Interface(object):

    def __init__(self, intname, targetName, portName):
        self.name     = intname
        self.target   = targetName
        self.baudrate = 57600
        self.port     = portName

    # Setters

    def setName(self, someName):
        self.name = someName

    def setTarget(self, targetName):
        self.target = targetName

    def setBaudRate(self, baudRate):
        self.baudrate = baudRate

    def setPort(self, portName):
        self.port = portName

    # Port Configuration

    def writePort(self):
        fname = '../config/targets/' + self.target + '/cmd_tlm_server.txt'
        f = open(fname, 'w')
        server_config = self.makeConfigStrings()

        for string in server_config:
            f.write(string)

        f.close()

    def makeConfigStrings(self):
        string1 = "INTERFACE " + self.target + " serial_interface.rb " + \
        self.port + " " + self.port + " " + str(self.baudrate) + \
        " NONE 1 10.0 nil LENGTH 0 8 0 1\n"

        string2 = "  TARGET " + self.target

        return [string1, string2]
