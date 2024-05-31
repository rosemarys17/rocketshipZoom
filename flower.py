import pygame
import random

class Flower:

    def __init__(self, x, y, flower_type):
        self.flower_type = flower_type
        self.x = x
        self.y = y
        self.image = pygame.image.load("black_flower.png")
        self.red = False
        self.set_image()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def set_image(self):
        if self.flower_type == 0:
            self.image = pygame.image.load("black_flower.png")
            self.red = False
        elif self.flower_type == 1:
            self.image = pygame.image.load("blue_flower.png")
            self.red = False
        elif self.flower_type == 2:
            self.image = pygame.image.load("purple_flower.png")
            self.red = False
        elif self.flower_type == 3:
            self.image = pygame.image.load("red_flower.png")
            self.red = True
        elif self.flower_type == 4:
            self.image = pygame.image.load("sunflower.png")
            self.red = False

    def draw_flower(self, screen):
        screen.blit(self.image, self.rect)
        
    def change(self, x, y):
        self.flower_type = random.randint(0,4)
        self.x = x
        self.y = y
        self.set_image()

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()