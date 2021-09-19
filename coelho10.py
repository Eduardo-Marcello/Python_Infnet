import pygame
from pygame.locals import *
import os.path
import math, random

LARGURA_TELA = 640
ALTURA_TELA = 480
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

def carregaImagens():
    global coelho, grama, castelo, flecha, inimigoImg, vidaBarra, vidaResto, gameover, ganhou
    
    filepath = os.path.dirname(__file__)
    coelho = pygame.image.load(os.path.join(filepath, "resources/images/dude.png"))
    grama = pygame.image.load(os.path.join(filepath, "resources/images/grass.png"))
    castelo = pygame.image.load(os.path.join(filepath, "resources/images/castle.png"))
    flecha = pygame.image.load(os.path.join(filepath, "resources/images/bullet.png"))
    inimigoImg = pygame.image.load(os.path.join(filepath, "resources/images/badguy.png"))
    vidaBarra = pygame.image.load(os.path.join(filepath, "resources/images/healthbar.png"))
    vidaResto = pygame.image.load(os.path.join(filepath, "resources/images/health.png"))
    gameover = pygame.image.load(os.path.join(filepath, "resources/images/gameover.png"))
    ganhou = pygame.image.load(os.path.join(filepath, "resources/images/youwin.png"))

def configuraSom():
    global hitSom, inimigoSom, tiroSom

    filepath = os.path.dirname(__file__)
    hitSom = pygame.mixer.Sound(os.path.join(filepath,"resources/audio/explode.wav"))
    inimigoSom = pygame.mixer.Sound(os.path.join(filepath, "resources/audio/enemy.wav"))
    tiroSom = pygame.mixer.Sound(os.path.join(filepath, "resources/audio/shoot.wav"))
    hitSom.set_volume(0.05)
    inimigoSom.set_volume(0.05)
    tiroSom.set_volume(0.05)
    pygame.mixer.music.load(os.path.join(filepath, 'resources/audio/moonlight.wav'))
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

def desenharArena():
    carregaImagens()
    for x in range(LARGURA_TELA // grama.get_width()+1):
        for y in range(ALTURA_TELA // grama.get_height()+1):
            DISPLAYSURF.blit(grama, (x*100,y*100))
    for y in range(30,350,105):
        DISPLAYSURF.blit(castelo,(0,y))
    
    # Atualizar tempo restante
    font = pygame.font.Font(None, 24)
    texto = font.render(str((90000-pygame.time.get_ticks())//60000)+":"+str((90000-pygame.time.get_ticks())//1000%60).zfill(2), True, (0,0,0))
    textoRect = texto.get_rect()
    textoRect.topright = [635,5]
    DISPLAYSURF.blit(texto, textoRect)
    
    # Atualizar barra de vida
    DISPLAYSURF.blit(vidaBarra, (5,5))
    for valor in range(vida):
        DISPLAYSURF.blit(vidaResto, (valor+8,8))

def desenhaCoelho(coelhoPos):
    DISPLAYSURF.blit(coelho, (coelhoPos[0], coelhoPos[1]))
 
def moveCoelho(teclas, coelhoPos):
    if teclas[0] and coelhoPos[1] > 0:
        coelhoPos[1] -= 5
    elif teclas[2] and coelhoPos[1] < 420:
        coelhoPos[1] += 5
    if teclas[1] and coelhoPos[0] > 0:
        coelhoPos[0] -= 5
    elif teclas[3]and coelhoPos[0] < 570:
        coelhoPos[0] += 5
    return coelhoPos

def verificaTeclaDown(event, teclas):
    # Enquanto estiver pressionado, o coelho vai se mexer
    if event.type == pygame.KEYDOWN:
        if event.key == K_w:
            teclas[0] = True
        elif event.key == K_a:
            teclas[1] = True
        elif event.key == K_s:
            teclas[2] = True
        elif event.key == K_d:
            teclas[3] = True

def verificaTeclaUp(event, teclas):
    # No momento que parou de pressionar a tecla
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            teclas[0] = False
        elif event.key == pygame.K_a:
            teclas[1] = False
        elif event.key == pygame.K_s:
            teclas[2] = False
        elif event.key == pygame.K_d:
            teclas[3] = False                

def giraCoelho(mousePos, coelhoPos):
    global coelho
    X, Y = (mousePos[1] - (coelhoPos[1]), mousePos[0]-(coelhoPos[0]))
    anguloRadianos = math.atan2(X, Y)
    angulo = math.degrees(anguloRadianos)
    coelho = pygame.transform.rotozoom(coelho, -angulo, 1)

def desenhaFlecha(flechas):
    global flecha

    for bala in flechas:
        index = 0
        velx = math.cos(bala[0])*10
        vely = math.sin(bala[0])*10
        bala[1] += velx
        bala[2] += vely
        if (bala[1] <= 64) or (bala[1] > 640) or (bala[2] <= 64) or (bala[2] > 480):
            flechas.pop(index)
        index += 1
        for projectil in flechas:
            flecha_temp = pygame.transform.rotate(flecha, 360 - projectil[0] * 57.29)
            DISPLAYSURF.blit(flecha_temp, (projectil[1], projectil[2]))

def criaInimigos():
    if (random.randint(1,100) <= 5) or (len(inimigos) == 0):
        inimigos.append([640, random.randint(50,430)])

def moveInimigos():
    for inimigo in inimigos:
        inimigo[0] -= 7
        verificaColisao(inimigo)

def desenhaInimigos():
    for inimigo in inimigos:
        DISPLAYSURF.blit(inimigoImg, inimigo)

def verificaColisao(inimigo):
    global vida, acuracia

    inimigoRect = pygame.Rect(inimigoImg.get_rect())
    inimigoRect.top= inimigo[1]
    inimigoRect.left = inimigo[0]
    # Verifica com as flechas
    for bala in flechas:
        balarect = pygame.Rect(flecha.get_rect())
        balarect.left = bala[1]
        balarect.top = bala[2]
        if inimigoRect.colliderect(balarect):
            acuracia[0] += 1
            inimigos.remove(inimigo)
            flechas.remove(bala)
            # Inclui som
            inimigoSom.play()
            break
    # Colisão com o castelo
    if (inimigoRect.left < 64):
        vida -= random.randint(5, 20)
        inimigos.remove(inimigo)
        # Inclui som
        hitSom.play()

def verificaFim():

    if (acuracia[1] != 0):
        acuraciaFinal = acuracia[0]*1.0 / acuracia[1]*100
    else:
        acuraciaFinal = 0
    if (pygame.time.get_ticks() >= 90000):
        desenhaFim(acuraciaFinal, ganhou)
    if (vida <= 0):
        desenhaFim(acuraciaFinal, gameover)

def desenhaFim(acuraciaFinal, imagem):

    pygame.font.init()
    font = pygame.font.Font(None, 24)
    texto = font.render("Precisão: " + str(round(acuraciaFinal, 2)) + "%", True, (0,255,0))
    textoRect = texto.get_rect()
    textoRect.centerx = DISPLAYSURF.get_rect().centerx
    textoRect.centery = DISPLAYSURF.get_rect().centery+24
    DISPLAYSURF.blit(imagem, (0,0))
    DISPLAYSURF.blit(texto, textoRect)

def main():
    pygame.init()
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    teclas = [False, False, False, False]
    coelhoPos = [100,100]
    mousePos = [100,100]
    global acuracia
    acuracia = [0, 0]
    global flechas
    flechas = []
    global inimigos
    inimigos = [[640,100]]
    global vida
    vida = 196
    pygame.display.set_caption("Mamãe Coelho")
    # Configura som
    configuraSom()

    terminou = False
    while not terminou:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminou = True
        verificaTeclaDown(event, teclas)
        verificaTeclaUp(event, teclas)
        if event.type == pygame.MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Inclui o som
            tiroSom.play()
            clickPos = pygame.mouse.get_pos()
            acuracia[1] += 1
            flechas.append([math.atan2(clickPos[1] - (coelhoPos[1] + 32), clickPos[0] - (coelhoPos[0] + 32)), \
                coelhoPos[0] + 32, coelhoPos[1] + 32])            
        desenharArena()
        coelhoPos = moveCoelho(teclas, coelhoPos)
        giraCoelho(mousePos, coelhoPos)
        desenhaCoelho(coelhoPos)
        desenhaFlecha(flechas)
        criaInimigos()
        moveInimigos()
        desenhaInimigos()
        verificaFim()
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()

if __name__=='__main__':
    main()