def potencia(numero_def, numero_potencia_def):
    resultado = 1
    f = 1
    while f <= numero_potencia_def:
        resultado *= numero_def
        f += 1
    print(resultado)


numero = int(input("Digite um numero inteiro qualquer: "))
numero_potencia = int(input("Digite a potencia do numero digitado: "))
potencia(numero, numero_potencia)
