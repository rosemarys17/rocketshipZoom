import pygame

class Bee:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("bee.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .5
        picture = pygame.image.load("bee.png")
        picture = pygame.transform.scale(picture, (1280, 720))

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


