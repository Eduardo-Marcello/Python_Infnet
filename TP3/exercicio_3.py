def adicionar_lista(lista_def):
    f = 0
    while f != 1:
        var = input("Digite qualquer palavra desejada, digite 0 para encerrar: ")
        if var == '0':
            f = 1
        else:
            lista_def.append(var)


lista = []
adicionar_lista(lista)
print(lista)
print(lista[::-1])
