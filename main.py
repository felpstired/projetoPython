# PROJETO: JOGO ATARI (ou algo parecido)
# LINGUAGEM UTILIZADA: PYTHON + BIBLIOTECA PYGAME

import pygame
import random
from sys import exit


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
fontB = pygame.font.Font('./fonts/minecrafter.reg.TTF', 60)


# IMAGENS

# pegar uma imagem e deixar ela do tamanho da janela
bgImg = pygame.image.load('./img/fundo.PNG').convert_alpha()
bg = pygame.transform.scale(bgImg, (x,y))

# pegar uma imagem e deixar ela menor pra ser usada como personagem
pImg = pygame.image.load('./img/player.png').convert_alpha()
p = pygame.transform.scale(pImg, (140,140))
p = pygame.transform.flip(p, True, False)

# 
propImg = pygame.image.load('./img/projetil.PNG').convert_alpha()
prop = pygame.transform.scale(propImg, (65, 65))

# 
enemyImg = pygame.image.load('./img/inimigo.PNG').convert_alpha()
enemy = pygame.transform.scale(enemyImg, (100, 100))

# 
bossImg = pygame.image.load('./img/boss.PNG').convert_alpha()
boss = pygame.transform.scale(bossImg, (400, 630))

# 
lifeImg = pygame.image.load('./img/life.PNG').convert_alpha()
lifeImg = pygame.transform.scale(lifeImg, (32, 32))


# faz o programa esperar um tempo antes de ser executado
# pygame.time.wait(50)


# POSIÇÕES

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

# tamanho do boss e a posição dele
bX = enemy.get_rect().width
bY = enemy.get_rect().height
posBY = 45
posBX = 900


# quadrados das colisões
colPlayer = p.get_rect()
colProp = prop.get_rect()
colEnemy = enemy.get_rect()
colBoss = boss.get_rect()


# VARIAVEIS IMPORTANTES

running = True

# define a velocidade do player
vel = 1

triggerProp = False

pontos = 0

life = 3
lifeB = 100

respawnP = False

def respawn():
    
    x = 1300
    y = random.randint(1, 640)
    
    return [x, y]


def respawnProp():
    
    triggerProp = False
    respawnPropX = positionPX
    respawnPropY = positionPY
    velPropX = 0
    
    return [(respawnPropX + 35), (respawnPropY + 40), triggerProp, velPropX]


def respawnPlayer(textY):

    gameRespawn = font.render('Aperte ENTER para reiniciar ou ESC para sair', True, ('white'))
    gameRespawnX = gameRespawn.get_rect().width
    screen.blit(gameRespawn, (640 - (gameRespawnX / 2), textY + 20))

    return True
    

def propCol():
    
    global life
    global pontos
    global lifeB
    global positionEX
    global positionEY
    global posPropX
    global posPropY
    global triggerProp
    global velProp
    
    if life > 0:

        if colProp.x == 1300:
            posPropX = respawnProp()[0]
            posPropY = respawnProp()[1]
            triggerProp = respawnProp()[2]
            velProp = respawnProp()[3]
            return True

        if colProp.colliderect(colEnemy):
            positionEX = respawn()[0]
            positionEY = respawn()[1]

            pontos += 1
            return True
        
        if pontos >= 10:

            if colProp.colliderect(colBoss):
                posPropX = respawnProp()[0]
                posPropY = respawnProp()[1]
                triggerProp = respawnProp()[2]
                velProp = respawnProp()[3]

                pontos += 10
                lifeB -= 5
                return True
    
    else:
        
        return False


def enemyCol():
    
    global life
    global pontos

    if colEnemy.x <= 10:
        pontos -= 1
        
        return True

    elif colPlayer.colliderect(colEnemy):
        life -= 1
        
        return True
    
    else:
        
        return False

def lifesCount():
    
    global life
    global pontos
    global respawnP

    for i in range(0, life):
        screen.blit(lifeImg, (50 + i * 30, 50))
    
    if life <= 0:
        gameOver = fontGO.render('GAME OVER', True, (255,0,0))
        gameOverX = 640 - ((gameOver.get_rect().width) / 2)
        gameOverY = 360 - ((gameOver.get_rect().height) / 2)
        screen.blit(gameOver, (gameOverX, gameOverY))
        respawnPlayer(gameOverY + gameOver.get_rect().height)
        respawnP = True
        
        return True

    elif pontos < 0:
        gameOver = fontGO.render('GAME OVER', True, (255,0,0))
        gameOverX = 640 - ((gameOver.get_rect().width) / 2)
        gameOverY = 360 - ((gameOver.get_rect().height) / 2)
        screen.blit(gameOver, (gameOverX, gameOverY))
        respawnPlayer(gameOverY + gameOver.get_rect().height)
        respawnP = True
        
        return True
    
    elif lifeB == 0 and life > 0:
        gameWin = fontGO.render('CONGRATULATIONS', True, (0,255,0))
        gameWinX = 640 - ((gameWin.get_rect().width) / 2)
        gameWinY = 360 - ((gameWin.get_rect().height) / 2)
        screen.blit(gameWin, (gameWinX, gameWinY))
        respawnPlayer(gameWinY + gameWin.get_rect().height)
        respawnP = True
        
        return True
    
    else:
        
        return False
    

def exit_game():
    
    running = False
    pygame.quit()
    exit()


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

    if life > 0:

        if positionEX <= 10 or enemyCol():
            positionEX = respawn()[0]
            positionEY = respawn()[1]
        
        if posPropX > 1280 or propCol():
            posPropX = respawnProp()[0]
            posPropY = respawnProp()[1]
            triggerProp = respawnProp()[2]
            velProp = respawnProp()[3]

    
    x -= 1

    if pontos < 10 and life > 0:
        positionEX -= 1.5
    elif pontos > 10 and life > 0:
        positionEX -= 3
    
    posPropX += velProp
    

    # fazer a colisão seguir as imagens
    colPlayer.x = positionPX
    colPlayer.y = positionPY
    
    colProp.x = posPropX
    colProp.y = posPropY
    
    colEnemy.x = positionEX
    colEnemy.y = positionEY

    colBoss.x = posBX + 70
    colBoss.y = posBY

    # DESENHAR AS COLISÕES NA TELA (TESTES)
    pygame.draw.rect(screen, (255, 0, 0), colPlayer, 3)
    pygame.draw.rect(screen, (255, 0, 0), colProp, 3)
    pygame.draw.rect(screen, (255, 0, 0), colEnemy, 3)


    screen.blit(prop, (posPropX, posPropY))
    screen.blit(p, (positionPX,positionPY))
    screen.blit(enemy, (positionEX,positionEY))


    if pontos >= 10:
        pygame.draw.rect(screen, (255, 0, 0), colBoss, 3)
        screen.blit(boss, (posBX,posBY))
        lifeBTela = fontB.render(f' BOSS: {int(lifeB)}%', True, (255,0,0))
        lifeBTelaX = lifeBTela.get_rect().width
        screen.blit(lifeBTela, (640 - (lifeBTelaX / 2), 50))
        

    if lifeB == 0:
        posBX += 10
        posBY += 10
    
    
    if respawnP:
        
        if keys[pygame.K_RETURN]:
            
            running = True
            vel = 1
            triggerProp = False
            pontos = 0
            life = 3
            lifeB = 100
            respawnP = False
            
        elif keys[pygame.K_ESCAPE]: 
            exit_game()


    # vida e pontuação
    lifesCount()

    score = font.render(f' SCORE: {int(pontos)}', True, ('white'))
    screen.blit(score, (1000, 50))        

    # fazer o jogo se atualizar repetidamente
    pygame.display.update()
    

# ONDE SERIA SUPOSTO PARA CHAMAR A MAIN DO PROJETO (MAS NAO APRENDI A DELIMITAR O LOOP AINDA)

# if __name__ == "__main__":
#     main()

#  >>>> ANOTAÇÕES >>>>

# ABENÇOADO SEJA ESSE SITE
# tem a lista para as teclas numericas
# https://stackoverflow.com/questions/54249410/num-pad-input-for-pygame


# ABENÇOADO SEJA ESSE SITE TAMBÉM
# tem a estrutura básica de um código em pygame
# https://stackoverflow.com/questions/1413937/how-is-this-basic-pygame-structure