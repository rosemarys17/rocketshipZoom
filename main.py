import pygame
from bee import Bee

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('snapitc', 15)
pygame.display.set_caption("AP CSP Pygame!")



# set up variables for the display
size = (700, 600)
screen = pygame.display.set_mode(size)
bee = Bee(70, 70)
background = pygame.image.load("background.png")

# render the text for later
display_title_screen1 = my_font.render("Use ASDW to move.", True, (0, 0, 0))
display_title_screen2 = my_font.render("Pollinate each colorful flower without",  True, (0, 0, 0))
display_title_screen3 = my_font.render("touching the black flowers! Don't let",  True, (0, 0, 0))
display_title_screen4 = my_font.render(" the bear steal your honey!", True, (0, 0, 0))
display_title_screen5 = my_font.render("Click the screen to begin!", True, (0, 0, 0))
title_screen = True
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        bee.move_direction("right")
    elif keys[pygame.K_LEFT]:
        bee.move_direction("left")
    elif keys[pygame.K_UP]:
        bee.move_direction("up")
    elif keys[pygame.K_DOWN]:
        bee.move_direction("down")

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            title_screen = False

    if title_screen:
        screen.fill((255, 192, 0))
        screen.blit(display_title_screen1, (125, 20))
        screen.blit(display_title_screen2, (40, 100))
        screen.blit(display_title_screen3, (45, 130))
        screen.blit(display_title_screen4, (70, 160))
        screen.blit(display_title_screen5, (45, 230))
    else:
        screen.blit(background, (0, -130))
        screen.blit(bee.image, bee.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
