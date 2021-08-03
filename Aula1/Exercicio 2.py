"""""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é 
aquele que é divisível somente por ele mesmo e por 1"""""
mult = 0

number = int(input("Enter a number: "))
for i in range(2,number):
    if(number % i == 0):
        mult += 1
if mult == 0:
    print("This number is prime")
else:
    print("This number is not prime")
