import os

list = os.listdir()

list_files = []
list_dir = []

for i in list:
    if os.path.isfile(i):
        list_files.append(i)
    else:
        list_dir.append(i)
if len(list_files) > 0:
    print("Files:")
    for i in list_files:
        print("\t" + i)
    print(" ")
if len(list_dir) > 0:
    print("Directories:")
    for i in list_dir:
        print("\t" + i)
    print(" ")
