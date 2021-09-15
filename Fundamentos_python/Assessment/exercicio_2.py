soma = 0
var = int(input("Digite um numero 'n' limite para a contagem [1 - n]: "))
for i in range(0, var + 1):
    if i % 2 == 0:
        soma += i
        print(soma)
print(soma)
