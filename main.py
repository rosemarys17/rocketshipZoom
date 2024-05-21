import pygame
from bee import Bee
from flower import Flower
import random

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('snapitc', 30)
pygame.display.set_caption("AP CSP Pygame!")



# set up variables for the display
size = (700, 600)
screen = pygame.display.set_mode(size)
bee = Bee(20, 250)
bee.rescale_image("bee.png")
background = pygame.image.load("background.png")
image_size = (800, 800)
background = pygame.transform.scale(background, image_size)
flower1 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower2 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower3 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower4 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower5 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower6 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower7 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower8 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower9 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower10 = Flower(random.randint(20,600), random.randint(250,560), random.randint(0,4))
flower1.rescale_image(flower1.image)
flower2.rescale_image(flower2.image)
flower3.rescale_image(flower3.image)
flower4.rescale_image(flower4.image)
flower5.rescale_image(flower5.image)
flower6.rescale_image(flower6.image)
flower7.rescale_image(flower7.image)
flower8.rescale_image(flower8.image)
flower9.rescale_image(flower9.image)
flower10.rescale_image(flower10.image)

# render the text for later
display_title_screen1 = my_font.render("Use ASDW to move.", True, (0, 0, 0))
display_title_screen2 = my_font.render("Pollinate each colorful flower without",  True, (0, 0, 0))
display_title_screen3 = my_font.render("touching the red flowers! Don't let",  True, (0, 0, 0))
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
        screen.blit(display_title_screen1, (180, 20))
        screen.blit(display_title_screen2, (20, 200))
        screen.blit(display_title_screen3, (30, 240))
        screen.blit(display_title_screen4, (105, 280))
        screen.blit(display_title_screen5, (100, 400))
    else:
        screen.blit(background, (0, -130))
        screen.blit(bee.image, bee.rect)
        screen.blit(flower1.image, flower1.rect)
        screen.blit(flower2.image, flower2.rect)
        screen.blit(flower3.image, flower3.rect)
        screen.blit(flower4.image, flower4.rect)
        screen.blit(flower5.image, flower5.rect)
        screen.blit(flower6.image, flower6.rect)
        screen.blit(flower7.image, flower7.rect)
        screen.blit(flower8.image, flower8.rect)
        screen.blit(flower9.image, flower9.rect)
        screen.blit(flower10.image, flower10.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
