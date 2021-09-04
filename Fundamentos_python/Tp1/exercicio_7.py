""""" Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma cumulativa;
isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original."""""


def cumsum(lista1_def):
    lista2_def = []
    for i in range(0, 6):
        soma = 0
        if i == 0:
            lista2_def.append(lista1_def[i])
        else:
            aux = lista1_def[i - 1]
            soma = lista1_def[i] + aux
            lista2_def.append(soma)
    return lista2_def


lista1 = [1, 2, 3, 4, 5, 6]
lista2 = cumsum(lista1)
print(lista1)
print(lista2)
