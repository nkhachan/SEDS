import glob
import serial

def getPorts():
    port_list = glob.glob ('/dev/tty[A-Za-z]*')
    cnt_ports = []
    for port in port_list:

        try:
            s = serial.Serial(port)
            s.close()
            cnt_ports.append(port)
        except serial.SerialException:
            pass

    return cnt_ports
