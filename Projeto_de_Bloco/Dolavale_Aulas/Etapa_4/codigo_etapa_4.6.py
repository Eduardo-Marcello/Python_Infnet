import psutil
import time
import subprocess


def show_info(pid):
    try:
        p = psutil.Process(pid)
        text = '{:6}'.format(pid)
        text = text + '{:11}'.format(p.num_threads())
        text = text + " " + time.ctime(p.create_time()) + " "
        text = text + '{:8.2f}'.format(p.cpu_times().user)
        text = text + '{:8.2f}'.format(p.cpu_times().system)
        text = text + '{:10.2f}'.format(p.memory_percent()) + " MB"
        rss = p.memory_info().rss / 1024 / 1024
        text = text + '{:10.2f}'.format(rss) + " MB"
        vms = p.memory_info().vms / 1024 / 1024
        text = text + '{:10.2f}'.format(vms) + " MB"
        text = text + " " + p.exe()
        print(text)
    except:
        pass


title = '{:^7}'.format("PID")
title = title + '{:^11}'.format("# Threads")
title = title + '{:^26}'.format("Creation")
title = title + '{:^9}'.format("T. Usu.")
title = title + '{:^9}'.format("T. Sis.")
title = title + '{:^12}'.format("Mem. (%)")
title = title + '{:^12}'.format("RSS")
title = title + '{:^12}'.format("VMS")
title = title + " Name"
print(title)

list = psutil.pids()

for i in list:
    show_info(i)
