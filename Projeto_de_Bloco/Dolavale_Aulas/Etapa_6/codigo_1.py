import socket
import os
import subprocess
import platform

hostname = socket.gethostname()
plataforma = platform.system()
args = []
if plataforma == "Windows":
    args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]
else:
    args = ['ping', '-c', '1', '-W', '1', hostname]
ret_cod = subprocess.call(args,
                          stdout=open(os.devnull, 'w'),
                          stderr=open(os.devnull, 'w'))
