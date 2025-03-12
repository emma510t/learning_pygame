import pygame

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

MOOVE_BACK = -3
MOOVE_FRONT = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

player1 = pygame.Rect((300, 250, 50, 50))
obstacle = pygame.Rect((700, 250, 100, 100))

#create ghost yt: https://www.youtube.com/watch?v=tJiKYMQJnYg
ghost = pygame.image.load("images/ghostnotmine.png")
ghostRect = ghost.get_rect()
ghostMask = pygame.mask.from_surface(ghost)
maskImage = ghostMask.to_surface()

points = 0

## define font - u can also add bold=True and italic=True
Arial30 = pygame.font.SysFont("Arial", 30)
## You van add a non system font by adding it in the folder and using Font("nameoffile.ttf") instead of SysFont

## function to display text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


run = True

while run:
    screen.fill((0,0,0))
    #draw_text("Hello emar", Arial30, (255, 255, 255), 20, 20)
    screen.blit(maskImage, (0,0))
    playeOneColor = (255, 62, 173)
    draw_text(str(points), Arial30, (255, 255, 255), 20, 20)

    if player1.colliderect(obstacle): 
        playeOneColor = (173, 255, 62)
        points = points +1

    pygame.draw.rect(screen, playeOneColor, player1)
    pygame.draw.rect(screen, (0, 255, 0), obstacle)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player1.move_ip(MOOVE_BACK, 0)
    elif key[pygame.K_d] == True:
        player1.move_ip(MOOVE_FRONT, 0)
    if key[pygame.K_w] == True:
        player1.move_ip(0, MOOVE_BACK)
    elif key[pygame.K_s] == True:
        player1.move_ip(0, MOOVE_FRONT)

    if points > 100:
        #run = False
        playeOneColor = (62, 173, 255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()