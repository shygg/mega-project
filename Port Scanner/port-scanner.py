#Port Scanner

import socket

ip = "192.168.1.1"
s = socket.socket(2, 1)
socket.setdefaulttimeout(2)


def porttry(ip, port):
    try:
        s.connect(ip, port)
        return True
    except:
        return None


for port in range(0, 10000):
    value = porttry(ip, port)
    if value is None:
        print("%d not open" % port)
    else:
        print("%d open!" % port)
        break

input()