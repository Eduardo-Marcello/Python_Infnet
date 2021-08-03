"""""Escreva uma função em Python que calcule o fatorial de um dado número N usando um for. O fatorial de 
N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. Por exemplo, para N=5 o 
fatorial é: 5 x 4 x 3 x 2 x 1 = 120. Se N for negativo, exiba uma mensagem indicando que não é possível 
calcular seu fatorial."""""


def calcularFatorial(aux_def):
    calculo = 1
    for i in range(aux_def, 1, -1):
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
