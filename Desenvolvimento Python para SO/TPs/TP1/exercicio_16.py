"""""Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo."""""
import psutil

for i in psutil.cpu_times(percpu=True):
    print(i)
