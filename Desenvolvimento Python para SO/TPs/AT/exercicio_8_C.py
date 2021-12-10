from random import randint
import time
import multiprocessing


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return fat


def calc(inn, out):
    fact_list = inn.get()
    vet = []
    for item in fact_list:
        factorial = fatorial(item)
        vet.append(factorial)
    out.put(vet)


N = 10000000
vetA = []
vetB = []
start = time.time()

if __name__ == "__main__":

    for i in range(N):
        vetA.append(randint(1, 10))

    process_number = 4

    inn = multiprocessing.Queue()
    out = multiprocessing.Queue()

    list_proc = []
    for i in range(process_number):
        init = i * int(N / process_number)
        final = (i + 1) * int(N / process_number)
        inn.put(vetA[init:final])
        m = multiprocessing.Process(target=calc, args=(inn, out))
        m.start()
        list_proc.append(m)

    for m in list_proc:
        m.join()
    end = float(time.time())
    print(f"\nTime: {round(end - start, 2)}")
