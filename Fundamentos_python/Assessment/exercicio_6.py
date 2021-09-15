def criar_tupla():
    lista_def = []
    f = 0
    while f != 1:
        var = int(input("Digite o valor desejado, digite 9999 para encerrar: "))
        if var == 9999:
            f = 1
        else:
            lista_def.append(var)
    return tuple(lista_def)


def separar_par_impar(tuplar_def):
    lista_def = []
    lista_tupla = []
    for i in range(len(tuplar_def)):
        if tuplar_def[i] % 2 != 0:
            lista_def.append(tuplar_def[i])
        elif tuplar_def[i] % 2 == 0:
            lista_tupla.append(tuplar_def[i])

    return lista_def, tuple(lista_tupla)


tuplar = criar_tupla()
lista, tupla2 = separar_par_impar(tuplar)
print(tuplar)
print(lista)
print(tupla2)
