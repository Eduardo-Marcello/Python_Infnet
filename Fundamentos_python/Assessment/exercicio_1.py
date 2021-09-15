def criar_tupla():
    lista = []
    f = 0
    while f != 1:
        var = int(input("Digite o valor desejado, digite 9999 para encerrar: "))
        if var == 9999:
            f = 1
        else:
            lista.append(var)
    print(lista)
    return tuple(lista)


tuplar = criar_tupla()
print(sorted(tuplar))
