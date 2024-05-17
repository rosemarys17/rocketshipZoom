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
        self.current_direction = "right"

    def move_direction(self, direction):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
        if direction == "right":
            self.x = self.x + self.delta
            self.current_direction = "right"
        if direction == "left":
            self.x = self.x - self.delta
            self.current_direction = "left"
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()