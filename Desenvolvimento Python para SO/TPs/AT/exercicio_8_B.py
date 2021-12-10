from random import randint
import time
from threading import Thread


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return fat


def calc(vetA, init, final, vetB):
    for item in vetA[init:final]:
        factorial = fatorial(item)
        vetB.append(factorial)


def thread_action(vetA, thread_num, N, thread_list, vetB):
    for i in range(thread_num):
        init = i * int(N/thread_num)
        final = (i + 1) * int(N/thread_num)
        t = Thread(target=calc, args=(vetA, init, final, vetB))
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print(vetB)


start = time.time()
N = 10000000
vetA = []
vetB = []
thread_list = []
thread_num = 4

for i in range(N):
    vetA.append(randint(1, 10))

thread_action(vetA, thread_num, N, thread_list, vetB)
end = time.time()
print(f"\nTime: {round(end - start, 2)}")
