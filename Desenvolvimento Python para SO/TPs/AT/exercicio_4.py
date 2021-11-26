"""""Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso"""""

for line in reversed(open("exercicio_4.txt").readlines()):
    print(line.rstrip()[::-1])
