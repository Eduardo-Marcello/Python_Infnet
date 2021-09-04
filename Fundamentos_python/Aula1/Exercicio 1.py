"""""Faça um programa que peça 3 números inteiros, calcule e mostre a quantidade de 
números pares e a quantidade de números impares."""""
even = 0
odd = 0

number1 = (int(input("Enter the first number: ")))
number2 = (int(input("Enter the second number: ")))
number3 = (int(input("Enter the third number: ")))
if number1 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
if number2 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
if number3 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1
print(f"The amount of even numbers: {even}")
print(f"The amount of odd numbers: {odd}")
