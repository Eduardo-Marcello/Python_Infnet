"""""Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos
deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando 
for lido um número negativo."""""
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

number = int(input("Digite um número inteiro positivo: "))
while number >= 0:
    for i in range(0, 25):
        if number == i:
            intervalo1 += 1
    for i in range(26, 50):
        if number == i:
            intervalo2 += 1
    for i in range(51, 75):
        if number == i:
            intervalo3 += 1
    for i in range(76, 100):
        if number == i:
            intervalo4 += 1
    number = int(input("Digite um número inteiro positivo: "))
print("Numero negativo detectado! Encerrando o loop...")
print(f"\nQuantidade de numeros no intervalo de [0-25] é {intervalo1}")
print(f"Quantidade de numeros no intervalo de [26-50] é {intervalo2}")
print(f"Quantidade de numeros no intervalo de [51-75] é {intervalo3}")
print(f"Quantidade de numeros no intervalo de [76-100] é {intervalo4}")
