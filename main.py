# hehehehe

import pygame

pygame.init()

# tamanho da tela
x = 1280
y = 720

screen = pygame.display.set_mode((x,y))

# definir o nome da janela
pygame.display.set_caption('Pizzaria')

# definir o icon da janela
iconJanela = pygame.image.load('./img/icon.png')
pygame.display.set_icon(iconJanela)

# pegar uma imagem e deixar ela do tamanho da janela
bgImg = pygame.image.load('./img/fundo.jpg').convert_alpha()
bg = pygame.transform.scale(bgImg, (x,y))

# pegar uma imagem e deixar ela menor pra ser usada como personagem
pImg = pygame.image.load('./img/fundo.jpg').convert_alpha()
p = pygame.transform.scale(pImg, (100,100))
p = pygame.transform.rotate(p, -90)

# pygame.time.wait(50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0,0))

    # pygame.display.flip()

    xRel = x % bg.get_rect().width
    screen.blit(bg, (xRel - bg.get_rect().width, 0))

    if xRel < 1280:
        screen.blit(bg, (xRel, 0))

        x -= 1

    # pygame.time.wait(50)
    # screen.fill('black')
    # pygame.display.flip()

    # pygame.time.wait(50)
    # screen.blit(bgImg, (-200,-200))

    pygame.display.update()

pygame.quit()