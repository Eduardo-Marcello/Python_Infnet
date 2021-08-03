""""" Escreva um programa em Python que calcule o fatorial de um dado número N usando um while. 
Use as mesmas especificações do item anterior."""""


def calcularFatorial(aux_def):
    flag = 0
    calculo = 1
    while aux_def > flag:
        calculo *= aux_def
        aux_def -= 1
    return calculo


fatorial = 0

n = int(input("Digite um número inteiro qualquer: "))
if n > 0:
    aux = n
    fatorial = calcularFatorial(aux)
    print(f"O fatorial de {n} é {fatorial}")
else:
    print("Fatorial não é calculado com números negativos")
