"""""Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo 
ou não. """""
import os

p = 'exercicio_1.py'
if os.path.isfile(p):
    print(p, 'é um arquivo!')
else:
    print(p, 'não é um arquivo!')

