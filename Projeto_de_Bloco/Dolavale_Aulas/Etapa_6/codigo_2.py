ip_string = input("Entre com o ip alvo: ")
ip_lista = ip_string.split('.')
base_ip = ".".join(ip_lista[0:3]) + '.'
print("O teste sera feito com a base: ", base_ip)
