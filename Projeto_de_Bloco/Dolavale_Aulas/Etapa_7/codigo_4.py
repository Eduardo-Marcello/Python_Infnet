import psutil
import socket


def obtem_nome_familia(familia):
    if familia == socket.AF_INET:
        return "IPv4"
    elif familia == socket.AF_INET6:
        return "IPv6"
    elif familia == socket.AF_UNIX:
        return "Unix"
    else:
        return "-"


def obtem_tipo_socket(tipo):
    if tipo == socket.SOCK_STREAM:
        return "TCP"
    elif tipo == socket.SOCK_DGRAM:
        return "UDP"
    elif tipo == socket.SOCK_RAW:
        return "IP"
    else:
        return "-"


for i in psutil.pids():
    p = psutil.Process(i)
    conn = p.connections()
    if len(conn) > 0:
        if conn[0].status.ljust(13) != "ESTABLISHED  ":
            endl = conn[0].laddr.ip.ljust(11)
            portl = str(conn[0].laddr.port).ljust(5)
            endr = conn[0].laddr.ip.ljust(13)
            portr = str(conn[0].laddr.port).ljust(5)
        print(str(i).ljust(5),
              " End.  Type   Status        Adress    Local   Port L.        Remote Adress  Port R.")
        print("      ", obtem_nome_familia(conn[0].family), " " + obtem_tipo_socket(conn[0].type),
              "   " + conn[0].status.ljust(13), endl, portl, "  " + endr, "  " + portr)
        print(" ")
