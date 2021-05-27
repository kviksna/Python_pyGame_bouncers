import pygame


pygame.init()
clock = pygame.time.Clock()

height = 400
width = 500

win = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("PyGame bounce pixel")

posX = 10
posY = 20
stepX = 2
stepY = 1

while True:
    # win.fill((0,0,0))  # black
    #pygame.draw.circle(win, (0,0,0), (posX, posY), 1)

    posX += stepX
    posY += stepY
    if posX > width or posX < 0:
        stepX *= -1
    if posY > height or posY < 0:
        stepY *= -1
    pygame.draw.circle(win, (0,255,0), (posX,posY), 1)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    clock.tick(120)  # FPS
