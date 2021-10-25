"""""Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path."""""
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
        print("\t" + j)
    print(" ")
