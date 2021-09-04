"""""Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
também pelo usuário, conforme exemplo abaixo:"""""

numero_tabuada = int(input("Entre com o valor da tabuada: "))
numero_inicio = int(input("Entre com o numero que a tabuada vai começar: "))
numero_final = int(input("Entre com o numero que a tabuada vai terminar: "))
index = numero_inicio
print(f"\nTabuada de {numero_tabuada}")
while index <= numero_final:
    print(f"{numero_tabuada} X {index} = {numero_tabuada * index}")
    index += 1
