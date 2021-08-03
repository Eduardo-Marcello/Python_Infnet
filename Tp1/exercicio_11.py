"""""Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que simule
o lançamento do dado e determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos."""""
from random import randint

lancamentos = []
count = 0

for i in range(0, 10):
    lancamentos.append(randint(1, 6))
print(lancamentos)
for i in range(len(lancamentos)):
    if lancamentos[i] == 6:
        count += 1
percentual = (count * 100) / 50
print(f"A porcentagem de vezes que a face 6 saiu é {percentual}%")
