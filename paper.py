import pygame
from random import randint
from constant_stuff import *

class Paper(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'light': self.image = pygame.image.load('images/paper_ball.png').convert_alpha()
        else: self.image = pygame.image.load('images/paper_ball2.png').convert_alpha()

        self.rect = self.image.get_rect(midbottom = (randint(60, WIDTH - 60), randint(-300, -60)))

    def destroy(self):
        if self.rect.y >= HEIGHT: self.kill()

    def update(self):
        self.rect.y += 5
        self.destroy()
