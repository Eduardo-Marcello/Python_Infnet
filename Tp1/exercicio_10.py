"""""Faça um programa que leia um vetor vet de 20 posições. O programa deve gerar, a partir do vetor lido,
 um outro vetor pos que contenha apenas os valores inteiros positivos de vet. A partir do vetor pos,
  deve ser gerado um outro vetor semdup que contenha apenas uma ocorrência de cada valor de pos."""""
vetor = []
vetor2 = []

for i in range(0, 6):
    numero = int(input("Digite um valor qualquer para o vetor: "))
    vetor.append(numero)

for i in range(len(vetor)):
        if vetor[i] > 0:
            vetor2.append(vetor[i])
vetor3 = set(vetor2)
print(vetor)
print(vetor2)
print(vetor3)