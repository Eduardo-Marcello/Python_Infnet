from random import randint

lancamentos = []
quantidade_lados = []
f = 0

while f < 6:
    quantidade_lados.append(0)
    f += 1
for i in range(0, 10):
    lancamentos.append(randint(1, 6))
print(lancamentos)
for i in range(len(lancamentos)):
    if lancamentos[i] == 1:
        quantidade_lados[0] += 1
    if lancamentos[i] == 2:
        quantidade_lados[1] += 1
    if lancamentos[i] == 3:
        quantidade_lados[2] += 1
    if lancamentos[i] == 4:
        quantidade_lados[3] += 1
    if lancamentos[i] == 5:
        quantidade_lados[4] += 1
    if lancamentos[i] == 6:
        quantidade_lados[5] += 1
print(f"A qauntidade de lados foi\n1 {quantidade_lados[0]}\n2 {quantidade_lados[1]}\n3 {quantidade_lados[2]}"
      f"\n4 {quantidade_lados[3]}\n5 {quantidade_lados[4]}\n6 {quantidade_lados[5]}")
