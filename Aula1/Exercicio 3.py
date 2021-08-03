"""""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
existentes entre 1 e um número inteiro informado pelo usuário."""""

index = 1
lista = []

final = int(input("Enter a number: "))
while index < final:
    count = 0
    for i in range(2, index):
        if index % i == 0:
            count += 1
    if count == 0:
        lista.append(index)
    index += 1

print("Prime numbers found")
print(lista)
