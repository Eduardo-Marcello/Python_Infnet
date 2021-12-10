from random import randint
import time


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return fat


def calc(vetA, init, final, vetB):
    for item in vetA[init:final]:
        factorial = fatorial(item)
        vetB.append(factorial)


N = 10000000
vetA = []
vetB = []
init = time.time()

for i in range(N):
    vetA.append(randint(1, 10))
for index in vetA:
    vetB.append(fatorial(index))
print(vetB)
final = time.time()
print(f"\nTime: {round(final - init, 2)}")
