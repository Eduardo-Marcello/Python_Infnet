"""""Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório."""""
import os

list = os.listdir()
dic_files = {}
for i in list:
    if os.path.isfile(i):
        ext = os.path.splitext(i)[1]
        if not ext in dic_files:
            dic_files[ext] = []
        dic_files[ext].append(i)
# print(dic_files)
for i in dic_files:
    print("Files: " + i)
    for j in dic_files[i]:
        status = os.stat(j)
        print(f"\t Nome:  {j}  || Size: {status.st_size}")
    print(" ")
