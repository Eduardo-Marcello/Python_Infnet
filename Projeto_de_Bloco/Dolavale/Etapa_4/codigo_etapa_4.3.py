import os

list = os.listdir()

dic_files = {}
list_dir = []
for i in list:
    if os.path.isfile(i):
        ext = os.path.splitext(i)[1]
        if not ext in dic_files:
            dic_files[ext] = []
        dic_files[ext].append(i)
    else:
        list_dir.append(i)
# print(dic_files)
for i in dic_files:
    print("Files: " + i)
    for j in dic_files[i]:
        print("\t" + j)
    print(" ")
if len(list_dir) > 0:
    print("Directories:")
    for i in list_dir:
        print("\t" + i)
    print(" ")
