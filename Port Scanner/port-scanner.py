#Port Scanner

import socket

ip = '127.0.0.1'
print("checking ip", ip)


def porttry(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.close
        return True
    except:
        return None


print(porttry(ip, 50007))


for port in range(75, 10000):
    value = porttry(ip, port)
    if value is None:
        #print("%d not open" % port)
        pass
    else:
        print("%d open!" % port)

input()