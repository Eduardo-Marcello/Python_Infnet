"""5. Trabalhar com tuplas é muito importante! Crie 4 funções nas quais:

1 - Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo
2 - Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
3 - Dada uma tupla e um elemento, elimine esse elemento da tupla.
4 - Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos."""


def localizar(tupla1_def, elemento):
    for i in range(len(tupla1_def)):
        if tupla1_def[i] == elemento:
            return i
    return -1


def divisao(tupla1_def):
    new_tupla = tupla1_def[:len(tupla1_def) // 2]
    return new_tupla


def divisao2(tupla1_def, tupla_meia_def):
    new_tupla = []
    index_def = 0
    while index_def < len(tupla1_def):
        if tupla1_def[index_def] not in tupla_meia_def:
            new_tupla.append(tupla1_def[index_def])
        index_def += 1
    return tuple(new_tupla)


def remove(tupla1_def, elemento):
    lista = list(tupla1_def)
    if elemento in lista:
        lista.remove(elemento)
    return tuple(lista)


def reverse(tupla1_def):
    tuplar = tupla1_def[::-1]
    return tuplar


tupla1 = (1, 2.5, 0, -7, -6.5, 12)

n1 = float(input("Digite um elemento qualquer: "))
index = localizar(tupla1, n1)
if index == -1:
    print("O elemento não existe na tupla")
else:
    print(f"O elemento foi encontado na posição {index}")
tupla_meia1 = divisao(tupla1)
print(tupla_meia1)
tupla_meia2 = divisao2(tupla1, tupla_meia1)
print(tupla_meia2)
n2 = float(input("Digite um elemento qualquer: "))
tupla1 = remove(tupla1, n2)
tupla_reverse = reverse(tupla1)
print(tupla_reverse)
