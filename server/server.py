import socket
from sql import *
from datetime import datetime

class Ipc:
    def __init__(self, host, port, name, con):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Connect(host, port)
        self.con = con

    def Connect(self, host, port):
        try:
            self.s.connect((host, port))
        except Exception as e:
            print(e)

    def run(self, diskinfo, ipslen):
        try:
            self.s.send(diskinfo.encode())
            free = self.s.recv(1000).decode()
            total = self.s.recv(1000).decode()
            virtualmf = self.s.recv(1000).decode()
            virtualmt = self.s.recv(1000).decode()
            swapmf = self.s.recv(1000).decode()
            swapmt = self.s.recv(1000).decode()
            print('------------DISK------------')
            print(total+' GB total on disk '+diskinfo)
            print(free+' GB free on disk '+diskinfo)
            print('----------------------------')
            print('-----------MEMORY------------------------')
            print(virtualmt+' GB total virtual memory on PC')
            print(virtualmf+' GB free virtual memory on PC')
            print(swapmt+' GB total swap memory on PC')
            print(swapmf+' GB free swap memory on PC')
            print('-----------------------------------------')

            current_datetime = datetime.now()

            print(self.con)
            print(ipslen)

            ins = 'INSERT INTO disk VALUES("'+str(ipslen)+'", "'+total+'", "'+free+'", "'+str(current_datetime)+'")'
            #sql_drop(self.con)
            sql_table(self.con, False, True, ins)
        except Error as e:
            print(e)
            print('Нудачно. Компьютер - '+str(ipslen + 1))

from config import *

ipslen = (len(ips) - 1)
#print('computers = '+str(len(ips)))

"""while ipslen >= 0:
    
    try:
        my_ipc = Ipc(ips[ipslen], ipsport[ipslen], ipslen, con)
    except:
        print('Компьютер выключен или программа не запущена!')
    try:
        diskinfo = ipsdisk[ipslen]
    except:
        diskinfo = 'C:'
    my_ipc.run(diskinfo)
    ipslen = ipslen - 1
    """