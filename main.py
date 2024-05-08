import pygame

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("AP CSP Pygame!")

# set up variables for the display
size = (400, 300)
screen = pygame.display.set_mode(size)

name = "Mr. Das"

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_title_screen1 = my_font.render("Use ASDW to move.", True, (255, 255, 255))
display_title_screen2 = my_font.render("Pollinate each colorful flower without touching the black flowers! Don't let the bear steal your honey!",  True, (255, 255, 255))
display_title_screen3 = my_font.render("Click anywhere on the screen to begin!", True, (255, 255, 255))
title_screen = True
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((90, 17, 146))
    if title_screen:
        screen.blit(display_title_screen1, (150, 200))
        screen.blit(display_title_screen2, (150, 230))
        screen.blit(display_title_screen3, (150, 260))

    screen.blit(display_name, (0, 0))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
