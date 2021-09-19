lista = []


def adicionar_item(lista_def):
    f = 0
    while f != 1:
        var = int(input("Digite o valor desejado, digite 9999 para encerrar: "))
        if var == 9999:
            f = 1
        else:
            lista_def.append(var)


adicionar_item(lista)
print(lista[::-1])
print(lista)
