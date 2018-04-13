import glob
import serial

temp_list = glob.glob ('/dev/tty[A-Za-z]*')
result = []
for a_port in temp_list:

    try:
        s = serial.Serial(a_port)
        s.close()
        result.append(a_port)
    except serial.SerialException:
        pass

for res in result:
    print (res)
