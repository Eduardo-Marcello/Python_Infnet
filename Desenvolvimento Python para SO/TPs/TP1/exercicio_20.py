"""""Escreva um programa em Python usando o módulo ‘psutil’, que imprima para a partição corrente:
a) o nome do dispositivo,
b) o tipo de sistema de arquivos que ela possui (FAT, NTFS, EXT, ...),
c) o total de armazenamento em GB e
d) o armazenamento disponível em GB."""""
import psutil

list = psutil.disk_partitions()
for i in list:
    disk_info = psutil.disk_usage(path=i[0])
    print(f"Device: {i[0]}")
    print(f"File system type: {i[2]}")
    print(f"Total size disk: {round(disk_info[0] / (1024 * 1024 * 1024), 2)} GB")
    print(f"Free size disk: {round(disk_info[2] / (1024 * 1024 * 1024), 2)} GB")
    print("------------------------\n")
