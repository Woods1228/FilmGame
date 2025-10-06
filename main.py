# & "C:/Users/Caden/Downloads/Game video gen pipeline/.venv/Scripts/python.exe" "watch_main.py"

import pygame
pygame.init()

screenWidth = 600
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))

startButton = pygame.Rect(250, 545, 100, 40)
background = pygame.image.load('Assets/start.png')
background = pygame.transform.scale(background, (screenWidth, screenHeight))

run = True

while run:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (138, 121, 93), startButton)
    pygame.display.update()

pygame.quit()