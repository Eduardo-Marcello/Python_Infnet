def adicionar_lista(lista_def):
    f = 0
    while f < 5:
        var = int(input("Digite o valor desejado: "))
        lista_def.append(var)
        f = f + 1


lista = []
adicionar_lista(lista)
print(lista)
