lista = []


def adicionar_lista(lista_def):
    f = 0
    while f != 1:
        var = int(input("Digite o valor desejado, digite 9999 para encerrar: "))
        if var == 9999:
            f = 1
        else:
            lista_def.append(var)


def remover_lista(lista_def):
    f = 0
    while f != 1:
        print(lista_def)
        var = int(input("Digite o valor que gostaria de retirar, digite 9999 para encerrar: "))
        if var == 9999:
            f = 1
        else:
            for i in range(len(lista_def)):
                if var == lista_def[i - 1]:
                    lista_def.remove(var)


adicionar_lista(lista)
print(lista)
remover_lista(lista)
print(lista)
print(len(lista))
