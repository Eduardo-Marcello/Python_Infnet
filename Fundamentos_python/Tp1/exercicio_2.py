"""""Faça uma função em Python que receba do usuário a idade de uma pessoa em anos, meses e dias e retorne essa 
idade expressa em dias. Considere que todos os anos têm 365 dias."""""
sub = 0

idade_anos = int(input("Digite quantos anos você possui: "))
idade_meses = int(input("Digite quantos meses passou do aniversário: "))
idade_dia = int(input("Digite quantos dias passaram:"))
idade_dias_totais = (idade_anos * 365) + (idade_meses * 31) + idade_dia
n = input("Algum mes que se passou tem menos de 31 dias? ")
if n == 'sim' or n == 's':
    n2 = int(input("Quantos? "))
    n3 = input("Desses meses que se passou, um era fevereiro? ")
    if n3 == 'sim' or n3 == 's':
        sub = 3
    sub = sub + n2
idade_dias_totais = idade_dias_totais - sub
input(f"O total de dias refrente a sua idade é {idade_dias_totais}")
