"""""Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo. A impressão não deve 
conter o nome do arquivo, apenas o caminho."""""
import os

file = 'arq_texto.txt'
path = os.path.split(os.path.abspath(file))
print(path[0])
