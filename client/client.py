import socket
import psutil

class Listener:
    def __init__(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((host, port))
        s.listen(1)
        print('Waiting...')
        self.conn, addr = s.accept()
        print('connect -', addr)

    def run(self):
        DISK = self.conn.recv(100).decode()
        free = psutil.disk_usage(DISK).free/(1024*1024*1024)
        total = psutil.disk_usage(DISK).total/(1024*1024*1024)
        virtualmf = psutil.virtual_memory().free/(1024*1024*1024)
        virtualmt = psutil.virtual_memory().total/(1024*1024*1024)
        swapmf = psutil.swap_memory().free/(1024*1024*1024)
        swapmt = psutil.swap_memory().total/(1024*1024*1024)
        self.conn.send(f"{free:.4}".encode())
        self.conn.send(f"{total:.4}".encode())
        self.conn.send(f"{virtualmf:.4}".encode())
        self.conn.send(f"{virtualmt:.4}".encode())
        self.conn.send(f"{swapmf:.4}".encode())
        self.conn.send(f"{swapmt:.4}".encode())
        self.conn.close()

while True:
    my_listener = Listener('localhost', 4443)
    my_listener.run()