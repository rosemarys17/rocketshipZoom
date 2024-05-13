import pygame
from bee import Bee

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("AP CSP Pygame!")

# set up variables for the display
size = (400, 300)
screen = pygame.display.set_mode(size)
bee = Bee(70,70)

# render the text for later
display_title_screen1 = my_font.render("Use ASDW to move.", True, (255, 255, 255))
display_title_screen2 = my_font.render("Pollinate each colorful flower without touching the black flowers! Don't let the bear steal your honey!",  True, (255, 255, 255))
display_title_screen3 = my_font.render("Click anywhere on the screen to begin!", True, (255, 255, 255))
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

    screen.fill((90, 57, 146))
    if title_screen:
        screen.blit(display_title_screen1, (150, 200))
        screen.blit(display_title_screen2, (150, 230))
        screen.blit(display_title_screen3, (150, 260))
    else:
        screen.blit(bee.image, bee.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
