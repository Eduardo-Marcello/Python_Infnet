def mostrar_lista(lista_def2):
    print(len(lista_def2))
    print(lista_def2)


def adicionar_lista(lista_def2):
    var = int(input("Digite o valor desejado: "))
    if len(lista_def2) == 0:
        lista_def2.append(var)
    else:
        for i in range(len(lista_def2)):
            if var == lista_def2[i - 1]:
                print("Número já existente!")
            else:
                lista_def2.append(var)


def remover_lista(lista_def2):
    var = int(input("Digite o valor que gostaria de retirar: "))
    for i in range(len(lista_def2)):
        if var == lista_def2[i - 1]:
            lista_def2.remove(var)


def remover_todos(lista_def2):
    lista_def2.clear()


def mensagem_sair():
    print("Saindo do Menu!")


def menu(lista_def):
    var = int(input("Menu\n[1] - Mostrar lista\n[2] - Incluir elemento\n[3] - Remover elemento\n[4] - Remover todos "
                    "os elementos da lista\n[5] - sair\nDigite sua opção: "))
    if var == 1:
        mostrar_lista(lista_def)
        return 1
    if var == 2:
        adicionar_lista(lista)
        return 2
    if var == 3:
        remover_lista(lista)
        return 3
    if var == 4:
        remover_todos(lista)
        return 4
    if var == 5:
        mensagem_sair()
        return 5


lista = []
opcao = 0

while opcao != 5:
    opcao = menu(lista)
print("Encerrando o programa...")
