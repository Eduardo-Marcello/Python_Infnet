"""""Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário, o tempo de criação e 
o uso de memória em KB."""""
import psutil
import time

print(psutil.pids())
pid = int(input("Digite o pid que queira verificar: "))
if psutil.pid_exists(pid):
    p = psutil.Process(pid)
    print(f"Nome do usuário: {p.username()} || Tempo de criação: {time.ctime(p.create_time())} || Uso de memória: {p.memory_percent()}")
else:
    print("processo inexistente!")
