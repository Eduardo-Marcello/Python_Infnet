var = 10
string = type(var)
print(f"{var}, {string}, {type(string)}")

if var > 3:
    print("Numero maior que 3")
elif (var > 0) and (var < 3):
    print("Numero maior que 0 e menor que 3")
elif var < 0:
    print("Numero negativo")
elif var == 3:
    print("Numero é 3")
else:
    print("Numero maior que 3")
