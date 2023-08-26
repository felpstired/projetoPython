# hehehehe

import pygame

pygame.init()

# tamanho da tela
x = 1280
y = 720

screen = pygame.display.set_mode((x,y))

# definir o nome da janela
pygame.display.set_caption("Freddy Fazbear's Pizzeria - ATARI")

# definir o icon da janela
iconJanela = pygame.image.load('./img/icon.png')
pygame.display.set_icon(iconJanela)

# pegar uma imagem e deixar ela do tamanho da janela
bgImg = pygame.image.load('./img/fundo.PNG').convert_alpha()
bg = pygame.transform.scale(bgImg, (x,y))

# pegar valor relativo de X pra poder fazer o fundo se mover


# pegar uma imagem e deixar ela menor pra ser usada como personagem
pImg = pygame.image.load('./img/player.png').convert_alpha()
p = pygame.transform.scale(pImg, (120,120))
p = pygame.transform.flip(p, True, False)


# 
propImg = pygame.image.load('./img/projetil.PNG').convert_alpha()
prop = pygame.transform.scale(propImg, (80, 80))


# 
enemyImg = pygame.image.load('./img/inimigo.PNG').convert_alpha()
enemy = pygame.transform.scale(enemyImg, (100, 100))


# faz o programa esperar um tempo antes de ser executado
# pygame.time.wait(50)


# tamanho do player e a posição dele
pX = p.get_rect().width
pY = p.get_rect().height
positionPY = (y / 2) - (pY / 2)
positionPX = 100

# tamanho do inimigo e a posição dele
eX = enemy.get_rect().width
eY = enemy.get_rect().height
positionEY = (y / 2) - (eY / 2)
positionEX = (x - 100) - (eX / 2)

# define a velocidade do player
vel = 10

triggerProp = False

running = True

# enquanto o jogo estiver aberto, roda o código abaixo

while running:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
# ^^ verificação para fechar a aba caso aperte em fechar ^^

    # mostra o background na tela
    screen.blit(bg, (0,0))
    
    # guarda a informação de qual tecla está sendo pressionada
    keys = pygame.key.get_pressed()
    # screen.blit(p, (0,0))

    # pygame.display.flip()

    # prop = pygame.transform.rotate(prop, 90)
    enemy = pygame.transform.rotate(enemy, 90)

    xRel = x % bg.get_rect().width
    screen.blit(bg, (xRel - bg.get_rect().width, 0))
    
    if xRel < 1280:
        screen.blit(bg, (xRel, 0))
        
        x -= 5


    
        

        
        
        # se a tecla de setinha pra cima for pressionada
        if keys[pygame.K_UP] and positionPY>0:
        
            # baixa na coordenada y
            positionPY -= vel
        
        # se a tecla de setinha pra cima for pressionada
        if keys[pygame.K_DOWN] and positionPY<y - pY:
        
            # aumento na coordenada y
            positionPY += vel    
        
        # se a tecla de setinha pra cima for pressionada
        if keys[pygame.K_SPACE]:
        
            # true se apertou
            triggerProp = True

            # velocidade do projetil
            velProp = 4
        

        screen.blit(p, (positionPX,positionPY))
        screen.blit(enemy, (positionEX,positionEY))
        # screen.blit(prop, (0,0))

    pygame.display.update()

pygame.quit()


#  >>>> ANOTAÇÕES >>>>

# ABENÇOADO SEJA ESSE SITE
# tem a lista para as teclas numericas
# https://stackoverflow.com/questions/54249410/num-pad-input-for-pygame

# if keys[pygame.K_RIGHT]:
#     x -= 10

# if keys[pygame.K_LEFT]: 
#     x += 2