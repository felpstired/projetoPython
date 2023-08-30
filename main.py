# PROJETO: JOGO ATARI (ou algo parecido)
# LINGUAGEM UTILIZADA: PYTHON + BIBLIOTECA PYGAME

import pygame
import random

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

# font = pygame.font.SysFont('impact', 30)
font = pygame.font.Font('./fonts/minecrafter.reg.TTF', 30)
fontGO = pygame.font.Font('./fonts/minecrafter.reg.TTF', 80)

# pegar uma imagem e deixar ela do tamanho da janela
bgImg = pygame.image.load('./img/fundo.PNG').convert_alpha()
bg = pygame.transform.scale(bgImg, (x,y))

# pegar uma imagem e deixar ela menor pra ser usada como personagem
pImg = pygame.image.load('./img/player.png').convert_alpha()
p = pygame.transform.scale(pImg, (120,120))
p = pygame.transform.flip(p, True, False)

# 
propImg = pygame.image.load('./img/projetil.PNG').convert_alpha()
prop = pygame.transform.scale(propImg, (65, 65))

# 
enemyImg = pygame.image.load('./img/inimigo.PNG').convert_alpha()
enemy = pygame.transform.scale(enemyImg, (100, 100))

# 
lifeImg = pygame.image.load('./img/life.PNG').convert_alpha()
lifeImg = pygame.transform.scale(lifeImg, (32, 32))


# faz o programa esperar um tempo antes de ser executado
# pygame.time.wait(50)

# tamanho do player e a posição dele
pX = p.get_rect().width
pY = p.get_rect().height
positionPY = (y / 2) - (pY / 2)
positionPX = 100

# tamanho do player e a posição dele
ppX = prop.get_rect().width
ppY = prop.get_rect().height
posPropX = (ppX / 2) + positionPX
posPropY = (ppY / 2) + positionPY
velProp = 0

# tamanho do inimigo e a posição dele
eX = enemy.get_rect().width
eY = enemy.get_rect().height
positionEY = (y / 2) - (eY / 2)
positionEX = (x - 100) - (eX / 2)


# quadrados das colisões
colPlayer = p.get_rect()
colProp = prop.get_rect()
colEnemy = enemy.get_rect()

# s = pygame.Surface((1000,750))  # the size of your rect
# s.set_alpha(128)                # alpha level
# s.fill((255,255,255))           # this fills the entire surface
# # screen.blit(s, (0,0)) 

# define a velocidade do player
vel = 1

triggerProp = False

running = True

pontos = 10

life = 4

# funcoes  
def propCol():
    global pontos
    
    if colPlayer.colliderect(colEnemy) or colEnemy.x <= 10:
        pontos -= 1
        return True
    
    else:
        return False

def lifeNEnemy():
    global life
    global pontos

    for i in range(0, life):
        screen.blit(lifeImg, (50 + i * 30, 50))
    
    if life <= 0:
        gameOver = fontGO.render('GAME OVER', True, (255,0,0))
        gameOverX = gameOver.get_rect().width
        gameOverY = gameOver.get_rect().height
        screen.blit(gameOver, (640 - (gameOverX / 2), 360 - (gameOverY / 2)))
        return True

    elif pontos <= 0:
        gameOver = fontGO.render('GAME OVER', True, (255,0,0))
        gameOverX = gameOver.get_rect().width
        gameOverY = gameOver.get_rect().height
        screen.blit(gameOver, (640 - (gameOverX / 2), 360 - (gameOverY / 2)))
        return True

    elif colPlayer.colliderect(colEnemy):
        life -= 1
        return True
    
    elif colProp.colliderect(colEnemy):
        pontos += 1
        return True
    
    else:
        return False

def respawn():
    x = 1300
    y = random.randint(1, 640)
    return [x, y]

def respawnProp():
    triggerProp = False
    respawnPropX = positionPX
    respawnPropY = positionPY
    velPropX = 0
    return [(respawnPropX + 30), (respawnPropY + 30), triggerProp, velPropX]


# enquanto o jogo estiver aberto, roda o código abaixo

while running:
    # pygame.time.delay(10)

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

    prop = pygame.transform.rotate(prop, 90)
    enemy = pygame.transform.rotate(enemy, -90)

    xRel = x % bg.get_rect().width
    screen.blit(bg, (xRel - bg.get_rect().width, 0))
    
    if xRel < 1280:
        screen.blit(bg, (xRel, 0))

        # se a tecla de setinha pra cima for pressionada
        if keys[pygame.K_UP] and positionPY>0:
        
            # baixa na coordenada y
            positionPY -= vel

            if not triggerProp:
                posPropY -= 1
        
        # se a tecla de setinha pra cima for pressionada
        if keys[pygame.K_DOWN] and positionPY<y - pY:
        
            # aumento na coordenada y
            positionPY += vel    

            if not triggerProp:
                posPropY += 1

        # se a tecla de setinha pra cima for pressionada
        if keys[pygame.K_RIGHT] and positionPX < 100:
        
            # baixa na coordenada y
            positionPX += vel

            if not triggerProp:
                posPropX += 1
        
        # se a tecla de setinha pra cima for pressionada
        if keys[pygame.K_LEFT] and positionPX > 0:
        
            # aumento na coordenada y
            positionPX -= vel    

            if not triggerProp:
                posPropX -= 1
        
        # se a tecla de setinha pra cima for pressionada
        if keys[pygame.K_SPACE]:
        
            # true se apertou
            triggerProp = True

            # velocidade do projetil
            velProp = 5

        
        if positionEX <= 10 or lifeNEnemy():
            positionEX = respawn()[0]
            positionEY = respawn()[1]
        
        if posPropX > 1280 or propCol():
            posPropX = respawnProp()[0]
            posPropY = respawnProp()[1]
            triggerProp = respawnProp()[2]
            velProp = respawnProp()[3]

        # if pontos == 0:
        #     running = False
        
        x -= 1
        positionEX -= 1.5
        posPropX += velProp
        
        colPlayer.x = positionPX
        colPlayer.y = positionPY
        
        colProp.x = posPropX
        colProp.y = posPropY
        
        colEnemy.x = positionEX
        colEnemy.y = positionEY

        score = font.render(f' SCORE: {int(pontos)}', True, ('white'))
        screen.blit(score, (1000, 50))

        # print(pontos)
        pygame.draw.rect(screen, (255, 0, 0), colPlayer, 3)
        pygame.draw.rect(screen, (255, 0, 0), colProp, 3)
        pygame.draw.rect(screen, (255, 0, 0), colEnemy, 3)
        

        screen.blit(prop, (posPropX, posPropY))
        screen.blit(p, (positionPX,positionPY))        
        screen.blit(enemy, (positionEX,positionEY))

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