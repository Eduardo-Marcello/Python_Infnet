frases = []
flag = 0
while flag != 1:
    frase = input("Digite uma frase qualquer: ")
    if frase == 'sair' or frase == 'Sair':
        flag = 1
    else:
        frases.append(frase)
if len(frases) == 0:
    print("Não possui frases cadastradas!")
else:
    print("\nFrases com a palavra [eu]:")
    for i in range(len(frases)):
        for j in frases[i].split():
            if j == "eu":
                print(frases[i])
