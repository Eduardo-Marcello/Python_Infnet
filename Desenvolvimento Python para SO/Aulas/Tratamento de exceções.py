import os

x = 'oi'
try:
    y = int(x)
    print(y)
except ValueError:
    pass

try:
    os.mkdir("exemplo")
    print("Diretorio criado com sucesso")
except FileExistsError:
    pass

try:
    open('workfile.txt', 'r')
except FileNotFoundError:
    pass

try:
    open('pasta', 'r')
except IsADirectoryError:
    pass

try:
    class z:
        def __init__(self, a, b):
            self.a = a
            self.b = b


    zz = z(1, 2)
    print(zz.c)
except AttributeError:
    pass

try:
    import psutill
except ModuleNotFoundError:
    raise

erro2 = [1, 2, 3, 4]

try:
    print(erro2[5])
except IndexError:
    pass
