"""""Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes, de segundo a segundo, o percentual 
do uso de CPU do computador."""""
import psutil, time

psutil.cpu_times(percpu=True)
for i in range(20):
  time.sleep(1)
  print(psutil.cpu_times(percpu=True))
