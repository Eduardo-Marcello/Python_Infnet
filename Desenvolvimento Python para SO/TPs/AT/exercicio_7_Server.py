import socket
import psutil
import pickle

mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mysocket.bind(('', 9090))

while True:
    (pacote, dest) = mysocket.recvfrom(1024)
    if pacote.decode('utf-8') == 'memory':
        msg_list = ['ACK']
        disk = psutil.disk_usage('.')
        used = disk.used / (1024 * 1024 * 1024)
        msg_list.append(round(used))
        total = disk.total / (1024 * 1024 * 1024)
        free = disk.free / (1024 * 1024 * 1024)
        msg_list.append(round(free))
        print(round(used), round(free),  round(total))
        mysocket.sendto(pickle.dumps(msg_list),  dest)
mysocket.close()
