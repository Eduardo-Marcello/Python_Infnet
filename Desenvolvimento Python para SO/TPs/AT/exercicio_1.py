"""""Escreva um programa em Python que:
1) Obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu 
   programa manipula suas informações;
2) Imprima o nome do processo e seu PID;
3) Imprima também o percentual de uso de CPU e de uso de memória."""""

import psutil


def show_process(pid):
    try:
        p = psutil.Process(pid)
        text = '{:4}'.format(pid)
        text = text + " " + '{:12}'.format(p.name())
        text = text + '{:12.2f}'.format(p.cpu_percent(interval=1.0))
        text = text + '{:12.2f}'.format(p.memory_percent())
        print(text)
    except:
        pass


list_pids = psutil.pids()

title = '{:^7}'.format("PID")
title = title + '{:^12}'.format("Name")
title = title + '{:^20}'.format("CPU (%)")
title = title + '{:^9}'.format("Mem. (%)")
print(title)
for i in list_pids:
    show_process(i)
