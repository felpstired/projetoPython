# trazer a biblioteca do pygame, constaantes e função de exit

import pygame
from pygame.locals import *
from sys import exit


# inicia o pygame

pygame.init()


# configurações e dados da janela

x = 640 ### largura da janela
y = 480 ### altura da janela
screen = pygame.display.set_mode((x,y)) ### setando a janela pra ter a altura definida acima
pygame.display.set_caption('Jogo Teste') ### definir o nome da janela

middleX = x / 2
middleY = y / 2

rectX = 600
rectY = 50
# circleR = 25

sqr = 45

sqrMiddle = middleX - (sqr / 2)

velX = middleX - (sqr / 2)
velY = y - sqr

jump = sqr * 3


font = pygame.font.SysFont('lucidasans', 20)
text = font.render('ABACAXI', True, (255,255,255))

# programa está setado para "em execução"

running = True


# o que vai acontecer enquanto o programa estiver em execução

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            exit() 
    
    screen.fill('white') ### preencher a tela com a cor branco
    
    rect = pygame.draw.rect(screen, (237, 67, 55), ((middleX - (rectX / 2)), 20, rectX, rectY), 0, 12)
    
    screen.blit(text, (rect.center))
    
    pygame.draw.rect(screen, (237, 67, 55), (velX, velY, sqr, sqr), 0, 12)
    
    # velY += 1
    
    # velX += 1
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and velY > 0:
        
        velY -= 0.5
        
    if keys[pygame.K_DOWN] and velY < y - sqr:
        velY += 0.5
        
    if keys[pygame.K_LEFT] and velX > 0:
        velX -= 0.5
        
    if keys[pygame.K_RIGHT] and velX < x - sqr:
        velX += 0.5
        
        
    # velY -= 2

    #     if velY == jump:
    #         velY += 2
        
    
    # if velY > y - sqr:
    #     velY = 0
    
    # pygame.draw.circle(screen, (237, 67, 55), ((middleX - (circleR / 2)), (rectY + 60)), circleR)
    # pygame.draw.line(screen, (237, 67, 55), (0, middleY), (x, middleY))
    # rect = pygame.draw.rect(screen, (255, 0, 255), ((middleX - (rectX / 2)), (rectY + 40), rectX, rectY))
    
    pygame.display.update()



    elif lifeB == 0 and life > 0:
        gameWin = fontGO.render('CONGRATULATIONS!!', True, (0,255,0))
        gameWinX = 640 - ((gameWin.get_rect().width) / 2)
        gameWinY = 360 - ((gameWin.get_rect().height) / 2)
        screen.blit(gameWin, (gameWinX, gameWinY))
        respawnPlayer(gameWinY)
        return True