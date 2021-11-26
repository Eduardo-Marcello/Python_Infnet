"""""Escreva um programa em Python que:
1) Gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles 
   ocupam em disco. Obtenha o nome do diretório do usuário.
2) Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort 
   ou sorted);
3) Gere um arquivo texto com os valores desta estrutura ordenados."""""

import os


def file_write(dir, list_arq_new):
    new_file = open('list_arqAndValues.txt', 'w')
    for i in list_arq_new:
        path = dir + str(i)
        new_file.write(f"{i}    {os.stat(path).st_size} \n")
    new_file.close()


#D:\\Users\\Eduardo\\Downloads\\
dir = input("Enter the diretory name: ")
if os.path.exists(dir):
    list_arq = []
    list_size = []
    list_arq_new = []
    list = os.listdir(dir)
    for i in list:
        path = dir + str(i)
        if os.path.isfile(path):
            list_arq.append(i)
            list_size.append(os.stat(path).st_size)
    list_size = sorted(list_size, reverse=True)
    for i in list_size:
        for j in list_arq:
            path = dir + str(j)
            if os.stat(path).st_size == i:
                list_arq_new.append(j)
    file_write(dir, list_arq_new)
else:
    print("The diretory doesn't exist.")
