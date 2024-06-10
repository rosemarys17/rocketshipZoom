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
my_font3 = pygame.font.SysFont('snapitc', 23)
pygame.display.set_caption("Pollinator Party!")



# set up variables for the display
honey = 0
size = (700, 600)
screen = pygame.display.set_mode(size)
bee = Bee(20, 250)
bear = Bear(100, 100)
bee.rescale_image("bee.png")
background = pygame.image.load("background.png")
image_size = (800, 800)
background = pygame.transform.scale(background, image_size)
flowers = []

current_time = time.time()
time_now = current_time
time_left = current_time
start_time = current_time + 10

for i in range(5):
    flower = Flower(random.randint(20, 500), random.randint(250, 500), random.randint(0, 4))
    flower.red = flower.red_check(flower.image)
    flowers.append(flower)

# render the text for later
display_welcome = my_font.render("Welcome to pollinator party!", True, (0, 0, 0))
display_continue = my_font.render("Click to continue!", True, (0, 0, 0))
display_title_screen1 = my_font.render("Use the arrow keys to move.", True, (0, 0, 0))
display_title_screen2 = my_font.render("Pollinate each colorful flower without",  True, (0, 0, 0))
display_title_screen3 = my_font.render("touching the red flowers! Don't let",  True, (0, 0, 0))
display_title_screen4 = my_font.render(" the bear steal your honey!", True, (0, 0, 0))
display_title_screen5 = my_font.render("Click the screen to begin!", True, (0, 0, 0))
display_honey = my_font3.render("Honey: " + str(honey), True, (0, 0, 0) )
display_bear = my_font3.render("Oh no! A bear got your honey!", True, (0, 0, 0) )
display_game_over = my_font3.render("You ran out of time! Total honey collected: " + str(honey), True, (0, 0, 0) )
title_screen = True
welcome = True
bear_bool = False
game_over = False
pygame.mixer.music.load('bgmusic.mp3')
collect_sound_bad = pygame.mixer.Sound("negative_sound_effect.wav")
collect_sound = pygame.mixer.Sound("sound_effect.wav")
pygame.mixer.music.play(-1)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:

    keys = pygame.key.get_pressed()
    display_honey = my_font3.render("Honey: " + str(honey), True, (0, 0, 0))
    display_time = my_font3.render("Time left: " + str(time_left) + "s", True, (255, 255, 255))

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
    if game_over:
        bear_bool = False
    if not welcome and not title_screen and int(time_left) < 19.5:
        for flower in flowers:
            if bee.rect.colliderect(flower.rect):
                flower.red_check(flower.image)
                if flower.red:
                    pygame.mixer.Sound.play(collect_sound_bad)
                    bear_bool = True
                    time_now = time_left
                else:
                    pygame.mixer.Sound.play(collect_sound)
                    honey = honey + 1
                flower.change(random.randint(20, 500), random.randint(250, 500))
    if time_left <= 0:
        game_over = True
        display_game_over = my_font3.render("You ran out of time! Total honey collected: " + str(honey), True, (250, 250, 250))
    if time_now == time_left + 1:
        bear_bool = False

    if game_over or (welcome and title_screen):
        bear_bool = False

    if title_screen:
        bear_bool = False
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
            honey = 0
            current_time = time.time()
            start_time = current_time + 20
            bear_bool = False

    else:
        if game_over:
            screen.fill((255, 192, 0))
            screen.blit(display_game_over, (15, 200))
        else:
            screen.blit(background, (0, -130))
            screen.blit(display_honey, (500, 20))
            screen.blit(display_time, (100, 20))
            screen.blit(bee.image, bee.rect)
            current_time = time.time()
            time_left = round(start_time - current_time, 2)

            for flower in flowers:
                screen.blit(flower.image, flower.rect)
        if bear_bool and not title_screen and not welcome:
            screen.blit(display_bear, (300, 200))
            screen.blit(bear.image, bear.rect)
            honey = 0
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
