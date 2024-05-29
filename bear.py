import pygame

class Bear:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("bear.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1
        picture = pygame.image.load("bear.png")
        picture = pygame.transform.scale(picture, (1280, 720))
        self.current_direction = "right"
