"""""Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes 
existem no vetor."""""
count = 0
index = 0
vetor = []

for i in range(0, 6):
    numero = float(input("Digite um valor qualquer para o vetor: "))
    vetor.append(numero)
while index < len(vetor):
    if vetor.count(vetor[index]) < 2:
        count += 1
    index += 1
print(f"A quantidade de números diferentes no vetor é {count}")
