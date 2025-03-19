import pygame
import time

pygame.init()

### size variables ########################################################

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

DIALOG_PADDING_x = 20
DIALOG_PADDING_b = DIALOG_PADDING_x
DIALOG_PADDING_t = SCREEN_HEIGHT/3*2-DIALOG_PADDING_b*2

DIALOG_BORDER_WIDTH = 6
DIALOG_INNER_BOX_PADDING_x = DIALOG_PADDING_x+DIALOG_BORDER_WIDTH
DIALOG_INNER_BOX_PADDING_t = DIALOG_PADDING_t+DIALOG_BORDER_WIDTH

DIALOG_OUTER_BOX_WIDTH = SCREEN_WIDTH-(DIALOG_PADDING_x*2)
DIALOG_OUTER_BOX_HEIGHT = SCREEN_HEIGHT-(SCREEN_HEIGHT/3*2-DIALOG_PADDING_b)
DIALOG_INNER_BOX_WIDTH = SCREEN_WIDTH-(DIALOG_PADDING_x*2)-(DIALOG_BORDER_WIDTH*2)
DIALOG_INNER_BOX_HEIGHT = SCREEN_HEIGHT-(SCREEN_HEIGHT/3*2-DIALOG_PADDING_b)-(DIALOG_BORDER_WIDTH*2)

DIALOG_TEXT_PADDING_x = DIALOG_INNER_BOX_PADDING_x + 10
DIALOG_TEXT_PADDING_t = DIALOG_INNER_BOX_PADDING_t + 10

### game fonts variables ############################################################

Arial30 = pygame.font.SysFont("Arial", 30)

### game color variables ############################################################

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

### game objects ############################################################

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

dialogborder = pygame.Rect((DIALOG_PADDING_x, DIALOG_PADDING_t, DIALOG_OUTER_BOX_WIDTH, DIALOG_OUTER_BOX_HEIGHT))
dialogbox = pygame.Rect((DIALOG_INNER_BOX_PADDING_x, DIALOG_INNER_BOX_PADDING_t, DIALOG_INNER_BOX_WIDTH, DIALOG_INNER_BOX_HEIGHT))

### functions ############################################################
## function to display text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

## function to display dialog text
def draw_dialog_text(text):
        draw_text(text, Arial30, WHITE, DIALOG_TEXT_PADDING_x, DIALOG_TEXT_PADDING_t)

## function to display dialog text typewriter
# def draw_typewriter_dialog_text(text):
#         text_array = list(text)
#         x = 0
#         for letter in text_array:
#             time.sleep(1)
#             x += 20
#             draw_text(letter, Arial30, WHITE, DIALOG_TEXT_PADDING_x + x, DIALOG_TEXT_PADDING_t)

run = True

while run:
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 255, 255), dialogborder)
    pygame.draw.rect(screen, (0, 0, 0), dialogbox)

    key = pygame.key.get_pressed()
    if key[pygame.K_n] == True:
        text_array = list("Am I in the dialog box?")
        x = DIALOG_TEXT_PADDING_x  
        for letter in text_array:
            pygame.time.delay(100)  
            draw_text(letter, Arial30, WHITE, x, DIALOG_TEXT_PADDING_t)
            pygame.display.update()  
            letter_width, _ = Arial30.size(letter)  
            x += letter_width  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    
    pygame.display.update()

pygame.quit()