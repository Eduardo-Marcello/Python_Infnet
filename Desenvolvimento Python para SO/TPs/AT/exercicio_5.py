import os


def readFiles():
    a = open(file1, "r")
    b = open(file2, "r")
    x = a.readlines()
    y = b.readlines()
    print(x, y, "\n")
    a.close()
    b.close()
    return x[0].split(' '), y[0].split(' ')


def countList(listA, listB):
    if len(listA) > len(listB):
        index = len(listA) - len(listB)
        while index != 0:
            listB.append('0')
            index -= 1
    else:
        index = len(listB) - len(listA)
        while index != 0:
            listA.append('0')
            index -= 1
    return listA, listB


def itemsAddUp(listA, listB):
    for i in range(len(listA)):
        print(f"{listA[i]} + {listB[i]} = {int(listA[i]) + int(listB[i])}")


# D:\\Users\\Eduardo\\Desktop\\a.txt
# D:\\Users\\Eduardo\\Desktop\\b.txt
file1 = input("Enter the file name: ")
file2 = input("Enter the file name: ")
if os.path.exists(file1) and os.path.exists(file2):
    listA, listB = readFiles()
    print(listA, listB, "\n")
    listA, listB = countList(listA, listB)
    print(listA, listB, "\n")
    itemsAddUp(listA, listB)
else:
    print("Arquivos não encontrados")
