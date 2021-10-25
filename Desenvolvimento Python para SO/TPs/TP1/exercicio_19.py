"""""Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento disponível há na 
partição do sistema (onde o sistema está instalado)."""""
import psutil

partitions = psutil.disk_partitions()
path = partitions[0][0]
disk_info = psutil.disk_usage(path=path)

print(f"Free disk size: {round(disk_info[2] / (1024 * 1024 * 1024), 2)} GB")
