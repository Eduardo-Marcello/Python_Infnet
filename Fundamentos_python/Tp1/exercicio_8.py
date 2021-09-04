"""""Um palíndromo é uma string que é lida da mesma forma do início para o fim e do fim para o início,
por exemplo, radar, toot e madam são palíndromos. Faça um algoritmo para validar se uma string é um palíndromo."""""

string = input("Digite uma palavra qualquer: ")
string_minuscula = string.lower()
string_invertida = string[:: -1]
if string_invertida == string_minuscula:
    print("A palavra digitada é um palídromo")
else:
    print("A palavra digitada não é um palídromo")