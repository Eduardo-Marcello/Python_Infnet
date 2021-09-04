"""""Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive. O número N 
deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma."""""

soma = 0
index = 0

n = int(input("Digite um número qualquer: "))
while index <= n:
    if index % 2 != 0:
        soma = soma + index
    index += 1
print(f"O somatório dos números impares é {soma}")
