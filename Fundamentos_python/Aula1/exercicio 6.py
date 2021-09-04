"""""Faça um programa que entre com um numero inteiro e imprima o primeiro numero (direita para esquerda)
do seu fatorial."""""
aux = 0
resposta = 1

number = int(input("Digite um número inteiro qualquer: "))
index = number
while index > 1:
    resposta = resposta * index
    if index == 2:
        aux = index
    index -= 1
print(f"Do número {number}, se obtem o fatorial {resposta}, cujo o primeiro numero (da direita para esuqerda) é {aux}")