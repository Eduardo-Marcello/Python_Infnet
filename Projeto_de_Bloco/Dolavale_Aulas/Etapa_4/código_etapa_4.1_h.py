import os
import time

list = os.listdir()

dic = {}
for i in list:
    if os.path.isfile(i):
        dic[i] = []
        dic[i].append(os.stat(i).st_size)
        dic[i].append(os.stat(i).st_atime)
        dic[i].append(os.stat(i).st_mtime)
title = '{:11}'.format("Size")
title = title + '{:27}'.format("Modification Date")
title = title + '{:27}'.format("Creation Date")
title = title + "Name"
print(title)
for i in dic:
    kb = dic[i][0] / 1000
    size = '{:10}'.format(str('{:.2f}'.format(kb) + ' KB'))
    print(size, time.ctime(dic[i][2]), " ", time.ctime(dic[i][1]), " ", i)
