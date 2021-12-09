import socket
import pickle
import sys

s_cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_cliente.settimeout(5)
dest = (socket.gethostname(), 9090)

user_input = input("Would you like to receive the memory (free and used) percentage?\nAnswer [Sim/Não]: ")
if user_input.lower() == 'sim':
    attempts = 1
    acknowledged = False
    msg = 'memory'
    while (attempts <= 5) and (not acknowledged):
        s_cliente.sendto(msg.encode('utf-8'), dest)
        try:
            msg_list, address = s_cliente.recvfrom(4069)
            acknowledged = True
        except socket.timeout:
            user_input = input("Want to try again?\nAnswer [Sim/Não]: ")
        if user_input.lower() == 'sim':
            attempts += 1
        elif user_input.lower() == 'não' or user_input.lower() == 'nao':
            print("Ending the program...")
            sys.exit(1)
        s_cliente.sendto(user_input.encode('utf-8'), dest)
    answer_list = pickle.loads(msg_list)
    if acknowledged:
        print(f"Used memory: {answer_list[1]} GB\nFree memory: {answer_list[2]} GB")
elif user_input.lower() == 'não' or user_input.lower() == 'nao':
    print("Ending the program...")
s_cliente.close()
