"""""Escreva um programa em Python que receba três valores reais X, Y e Z, guarde esses valores 
numa tupla e verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, 
neste caso, retorne qual o tipo de triângulo formado. 

Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: 
o comprimento de cada lado de um triângulo  deve ser menor do que a soma do comprimento dos outros 
dois lados. Além disso, o programa deve identificar o tipo de triângulo formado."""""
flag1 = 0
flag2 = 0
flag3 = 0
aux = 0

lado_a = float(input("Digite o valor do primeiro lado do triangulo: "))
lado_b = float(input("Digite o valor do segundo lado do triangulo: "))
lado_c = float(input("Digite o valor do terceiro lado lado do triangulo: "))

comprimento_ab = lado_a + lado_b
comprimento_bc = lado_b + lado_c
comprimento_ca = lado_c + lado_a

if lado_a < comprimento_bc:
    flag1 = 1
if lado_b < comprimento_ca:
    flag2 = 1
if lado_c < comprimento_ab:
    flag3 = 1

if flag1 == 1 or flag2 == 1 or flag3 == 1:
    print("Primeiro lado se encontra dentro dos requisitos")
    if (flag1 == 1 and flag2 == 1) or (flag1 == 1 and flag3 == 1) or (flag2 == 1 and flag3 == 1):
        print("Segundo lado se encontra dentro dos requisitos")
        if flag1 == 1 and flag2 == 1 and flag3 == 1:
            print("Terceiro lado se encontra dentro dos requisitos")
            aux = 1

if aux == 1:
    if lado_a == lado_b and lado_a == lado_c:
        print("O triângulo formado é equilátero")
    elif lado_a == lado_b or lado_b == lado_c:
        print("O triângulo formado é isósceles")
    else:
        print("O triângulo formado é escaleno")
else:
    print("Um lado não cumpriu os requisitos! Tente novamente!")
