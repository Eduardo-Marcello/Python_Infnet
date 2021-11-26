"""""Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa
do sistema Windows bloco de notas (notepad) para abrir o arquivo."""""

import os
import subprocess

arq_text = input("Enter the text file name: ")
if os.path.exists(arq_text):
 subprocess.run(["notepad.exe", arq_text])
else:
    print("The file doesn't exist.")
