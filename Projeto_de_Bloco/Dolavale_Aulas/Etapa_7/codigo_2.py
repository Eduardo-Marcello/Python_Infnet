import psutil
import time

io_status = psutil.net_io_counters(pernic=True)
nomes = []
for i in io_status:
    nomes.append(str(i))
for j in nomes:
    print(j)
    print("\t" + str(io_status[j]))
for i in range(4):
    time.sleep(1)
    io_status = psutil.net_io_counters(pernic=True)
    for j in nomes:
        print(j)
        print("\t" + str(io_status[j]))
