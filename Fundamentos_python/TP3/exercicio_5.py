alunos_altura = {}
f = 0


def mostrar_media(alunos_altura_def):
    media = 0
    for j in alunos_altura_def.values():
        media += j
    media = media / len(alunos_altura_def.values())
    for i, j in alunos_altura_def.items():
        if j > media:
            print(i)


while f != 1:
    key = input("Digite o nome do aluno: ")
    if key == 'sair' or key == 'Sair':
        f = 1
    else:
        alunos_altura[key] = float(input("Digite a altura deste aluno: "))
mostrar_media(alunos_altura)
