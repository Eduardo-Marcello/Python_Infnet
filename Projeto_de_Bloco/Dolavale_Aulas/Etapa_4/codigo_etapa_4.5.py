import psutil

name = input(" Enter the name of the process you wanted to search: ")
lp = psutil.pids()
list_pids = []
for i in lp:
    p = psutil.Process(i)
    if p.name() == name:
        list_pids.append(str(i))
if len(list_pids) > 0:
    print(f"The {name} PID(s) are: ")
    print(', '.join(list_pids))
else:
    print(f"{name} process is not running")