import socket
import pickle
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#D:\\Users\\Eduardo\\Downloads\\
try:
    print("Connecting to Server...")
    s.connect((socket.gethostname(), 9090))
    print("Sucess!")
    dir = input("Enter the diretory name: ")
    s.send(dir.encode('utf-8'))
    msg = s.recv(9000)
    if len(msg) > 27:
        list_files = pickle.loads(msg)
        for i in list_files:
            print(i)
    else:
        print(msg.decode('utf-8'))
except Exception as erro:
    print(str(erro))
    sys.exit(1)
