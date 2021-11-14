import socket
import sys
import pygame
import pickle


def machineInfo():
    def mostra_uso_memoria():
        req = 'mem'
        s.send(req.encode('utf-8'))
        s_msg = s.recv(1000)
        mem = pickle.loads(s_msg)
        larg = largura_tela - 2 * 20
        pygame.draw.rect(tela, azul, (20, 520, larg, 70))
        larg = larg * mem.percent / 100
        pygame.draw.rect(tela, vermelho, (20, 520, larg, 70))
        total = round(mem.total / (1024 * 1024 * 1024), 2)
        texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
        text = font.render(texto_barra, 1, branco)
        tela.blit(text, (20, 500))

    def mostra_uso_disco():
        req = 'disk'
        s.send(req.encode('utf-8'))
        s_msg = s.recv(1000)
        disk = pickle.loads(s_msg)
        larg = largura_tela - 2 * 20
        pygame.draw.rect(tela, azul, (20, 660, larg, 70))
        larg = larg * disk.percent / 100
        pygame.draw.rect(tela, vermelho, (20, 660, larg, 70))
        total = round(disk.total / (1024 * 1024 * 1024), 2)
        texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
        text = font.render(texto_barra, 1, branco)
        tela.blit(text, (20, 630))

    def mostra_ip():
        req = 'ip'
        s.send(req.encode('utf-8'))
        s_msg = s.recv(1000)
        ip = s_msg.decode('utf-8')
        text_barra = "IP: " + ip
        text = font.render(text_barra, 1, branco)
        tela.blit(text, (20, 460))

    def mostra_info_cpu():
        s1.fill(branco)
        mostra_texto(s1, "Nome:", "brand_raw", 10)
        mostra_texto(s1, "Arquitetura:", "arch", 30)
        mostra_texto(s1, "Palavra (bits):", "bits", 50)
        mostra_texto(s1, "Frequência (MHz):", "freq", 70)
        mostra_texto(s1, "Núcleos (físicos):", "nuc", 90)
        tela.blit(s1, (0, 0))

    def mostra_texto(s1_def, nome, chave, pos_y):
        text = font.render(nome, True, preto)
        s1_def.blit(text, (10, pos_y))
        req = chave
        if chave == "freq":
            s.send(req.encode('utf-8'))
            s_msg = s.recv(1000)
            cpu_info = s_msg.decode('utf-8')
        elif chave == "nuc":
            s.send(req.encode('utf-8'))
            s_msg = s.recv(1000)
            cpu_info = s_msg.decode('utf-8')
        else:
            s.send(req.encode('utf-8'))
            s_msg = s.recv(1000)
            cpu_info = s_msg.decode('utf-8')
        text = font.render(cpu_info, True, cinza)
        s1_def.blit(text, (160, pos_y))

    def mostra_uso_cpu(s1):
        s1.fill(cinza)
        req = 'cpu'
        s.send(req.encode('utf-8'))
        s_msg = s.recv(1000)
        l_cpu_percent = pickle.loads(s_msg)
        num_cpu = len(l_cpu_percent)
        x = y = 10
        desl = 10
        alt = (s1.get_height() - 2 * y) / 3
        larg = (s1.get_width() - 2 * y - (num_cpu + 1) * desl) / num_cpu
        d = x + desl
        for i in l_cpu_percent:
            pygame.draw.rect(s1, vermelho, (d, y, larg, alt))
            pygame.draw.rect(s1, azul, (d, y, larg, (1 - i / 100) * alt))
            d = d + larg + desl
        tela.blit(s1, (0, altura_tela / 5))

    preto = (0, 0, 0)
    branco = (255, 255, 255)
    cinza = (100, 100, 100)
    azul = (40, 40, 255)
    vermelho = (255, 0, 0)

    largura_tela = 1000
    altura_tela = 800
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Informações de CPU")
    pygame.display.init()
    s1 = pygame.surface.Surface((largura_tela, altura_tela))

    pygame.font.init()
    font = pygame.font.Font(None, 24)

    clock = pygame.time.Clock()
    cont = 60

    terminou = False
    while not terminou:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

        if cont == 60:
            mostra_info_cpu()
            mostra_uso_cpu(s1)
            mostra_ip()
            mostra_uso_memoria()
            mostra_uso_disco()
            cont = 0

        pygame.display.update()

        clock.tick(60)
        cont = cont + 1

    pygame.display.quit()
    return 0


def msgMenu():
    print("Menu Principal: \n"
          "[1] - Informações de Participação da Máquina \n"
          "[2] - Informações Referentes aos Diretórios e Arquivos \n"
          "[3] - Informações Referentes as Sub-Redes e suas Portas \n"
          "[4] - Informações Referentes a Rede \n"
          "[9] - Encerrar o programa \n")
    return input("Digite a opção desejada: ")


def menuPrincipal(option):
    if option == '1':
        controll = 1
        while controll == 1:
            controll = machineInfo()
        return 1
    elif option == '2':
        # dirAndFilesAndProcess()
        return 1
    elif option == '3':
        # ipsAndSub()
        return 1
    elif option == '4':
        # redesInfo()
        return 1
    elif option == '9':
        msg = 'sair'
        s.send(msg.encode('utf-8'))
        return 0


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
flag = 1

try:
    # Tenta se conectar ao servidor
    s.connect(("192.168.0.104", 9999))
except Exception as erro:
    print(str(erro))
    sys.exit(1)  # Termina o programa

while flag == 1:
    option = msgMenu()
    flag = menuPrincipal(option)
print("Encerrando o Programa...")
s.close()
