import pygame


pygame.init()
clock = pygame.time.Clock()

height = 400
width = 500

win = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("PyGame bounce line")

posX1 = 10
posX2 = 15
posY1 = 20
posY2 = 10
stepX1 = 2
stepX2 = 1
stepY1 = 1
stepY2 = 3

while True:
    # win.fill((0,0,0))  # black
    #pygame.draw.circle(win, (0, 0, 0), (posX1, posY1), 1)
    #pygame.draw.circle(win, (0, 0, 0), (posX2, posY2), 1)
    #pygame.draw.line(win, (0, 0, 0), (posX1, posY1), (posX2, posY2), 1)

    posX1 += stepX1
    posX2 += stepX2
    posY1 += stepY1
    posY2 += stepY2
    if posX1 > width or posX1 < 0:
        stepX1 *= -1
    if posX2 > width or posX2 < 0:
        stepX2 *= -1
    if posY1 > height or posY1 < 0:
        stepY1 *= -1
    if posY2 > height or posY2 < 0:
        stepY2 *= -1
    # pygame.draw.circle(win, (0, 255, 0), (posX1, posY1), 1)  # green
    # pygame.draw.circle(win, (255, 0, 0), (posX2, posY2), 1)  # red
    pygame.draw.line(win, (0, 255, 0), (posX1, posY1), (posX2, posY2), 1)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    clock.tick(240)  # FPS
