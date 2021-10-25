"""""Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’,
 de bloco de notas (notepad) para abri-lo."""""
import os

file = input("Digite o nome do arquivo texto que deseja abrir: ")
osCommandString = "notepad.exe " + file + ".txt"
os.system(osCommandString)
