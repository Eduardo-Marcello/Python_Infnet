def f(i):
    if i == 1 or i == 2:
        return 1
    return f(i - 1) + f(i - 2)


print(f(10))