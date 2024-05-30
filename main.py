import pygame
from bee import Bee
from flower import Flower
from bear import Bear
import time
import random

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('snapitc', 30)
my_font2 = pygame.font.SysFont('snapitc', 15)
pygame.display.set_caption("Pollinator Party!")



# set up variables for the display
score = 0
honey = score//3
size = (700, 600)
screen = pygame.display.set_mode(size)
bee = Bee(20, 250)
bear = Bear(random.randint(20, 400), random.randint(20, 400))
bee.rescale_image("bee.png")
background = pygame.image.load("background.png")
image_size = (800, 800)
background = pygame.transform.scale(background, image_size)
flowers = []
for i in range(10):
    flower = Flower(random.randint(20, 600), random.randint(250, 560), random.randint(0, 4))
    flower.rescale_image(flower.image)
    flowers.append(flower)

# render the text for later
display_welcome = my_font.render("Welcome to pollinator party!", True, (0, 0, 0))
display_continue = my_font.render("Click to continue!", True, (0, 0, 0))
display_title_screen1 = my_font.render("Use ASDW to move.", True, (0, 0, 0))
display_title_screen2 = my_font.render("Pollinate each colorful flower without",  True, (0, 0, 0))
display_title_screen3 = my_font.render("touching the red flowers! Don't let",  True, (0, 0, 0))
display_title_screen4 = my_font.render(" the bear steal your honey!", True, (0, 0, 0))
display_title_screen5 = my_font.render("Click the screen to begin!", True, (0, 0, 0))
display_honey = my_font2.render("Honey: " + str(honey), True, (0, 0, 0) )
display_bear = my_font2.render("Oh no! A bear got your honey!", True, (0, 0, 0) )
title_screen = True
welcome = True
start_time = time.time()
current_time = start_time
bear_bool = False

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:

    keys = pygame.key.get_pressed()
    display_honey = my_font2.render("Honey: " + str(honey), True, (0, 0, 0))

    if keys[pygame.K_RIGHT]:
        bee.move_direction("right")
    if keys[pygame.K_LEFT]:
        bee.move_direction("left")
    if keys[pygame.K_UP]:
        bee.move_direction("up")
    if keys[pygame.K_DOWN]:
        bee.move_direction("down")

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if welcome and title_screen:
                welcome = False
            elif title_screen and not welcome:
                title_screen = False

    for flower in flowers:
        if bee.rect.colliderect(flower.rect):
            print("Colliding with a flower")
        if flower.red == True:
            bear_bool = True
        else:
            score = score + 1
        honey = score//3

    if title_screen:
        if welcome:
            screen.fill((255, 192, 0))
            screen.blit(display_welcome, (100, 230))
            screen.blit(display_continue, (180, 270))
        else:
            screen.fill((255, 192, 0))
            screen.blit(display_title_screen1, (180, 20))
            screen.blit(display_title_screen2, (20, 200))
            screen.blit(display_title_screen3, (30, 240))
            screen.blit(display_title_screen4, (105, 280))
            screen.blit(display_title_screen5, (100, 400))
            score = 0
            honey = score//3
            start_time = time.time()
            current_time = start_time
    else:
        screen.blit(background, (0, -130))
        screen.blit(display_honey, (500, 20))
        screen.blit(bee.image, bee.rect)
        for flower in flowers:
            screen.blit(flower.image, flower.rect)
    if bear_bool and not title_screen and not welcome:
        screen.blit(bear.image, bear.rect)
        score = 0
        honey = score//3
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
