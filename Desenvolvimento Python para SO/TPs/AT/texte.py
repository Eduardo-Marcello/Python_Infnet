import os

a = "D:\\Users\\Eduardo\\Downs\\"

if os.path.exists(a):
    print(1)
else:
    print(2)

msg = "The diretory doesn't exist."

print(len(msg))