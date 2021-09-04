def adicionar_lista(lista_def, t_def):
    index = 0
    while index < t_def:
        var = float(input("Digite o valor desejado: "))
        lista_def.append(var)
        index += 1


def localiza_zero(lista_def):
    count_def = 0
    for i in range(len(lista_def)):
        if lista_def[i] == 0:
            count_def += 1
    return count_def


lista = []

t = int(input("Qual o tamanho que deseja que seu vetor tenha? \nDigite: "))
adicionar_lista(lista, t)
print(lista)
count = localiza_zero(lista)
print(f"A quantidade de 0 dentro do vetor é {count}")
