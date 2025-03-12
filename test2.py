import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = pygame.Rect((300, 250, 50, 50))
player2 = pygame.Rect((700, 250, 50, 50))

run = True

while run:
    #screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player1)
    pygame.draw.rect(screen, (0, 255, 0), player2)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player1.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player1.move_ip(1, 0)
    if key[pygame.K_w] == True:
        player1.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player1.move_ip(0, 1)
    if key[pygame.K_LEFT] == True:
        player2.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        player2.move_ip(1, 0)
    if key[pygame.K_UP] == True:
        player2.move_ip(0, -1)
    elif key[pygame.K_DOWN] == True:
        player2.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()