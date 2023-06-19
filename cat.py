import pygame
from constant_stuff import *

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.load_animation_images()
        self.gravity = 0
        self.animation_index = 0
        self.animation = False
        self.facing_right = False
        self.image = self.walking_animation_left[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (WIDTH/2, 375))


    def load_animation_images(self):
        self.jump_left = pygame.image.load('images/jump.png').convert_alpha()
        self.walk_1_left = pygame.image.load('images/cat1.png').convert_alpha()
        self.walk_2_left = pygame.image.load('images/cat2.png').convert_alpha()
        self.jump_right = pygame.image.load('images/jump_right.png').convert_alpha()
        self.walk_1_right = pygame.image.load('images/cat1_right.png').convert_alpha()
        self.walk_2_right = pygame.image.load('images/cat2_right.png').convert_alpha()
        self.walking_animation_left = [self.walk_1_left, self.walk_2_left]
        self.walking_animation_right = [self.walk_1_right, self.walk_2_right]

    def set_image(self, index):
        return self.walking_animation_right[int(index)] if self.facing_right else self.walking_animation_left[int(index)]

    def animate(self):
        if self.rect.bottom < 350:
            self.image = self.jump_right if self.facing_right else self.jump_left

        if self.animation:
            self.animation_index += 0.1
            if self.animation_index > len(self.walking_animation_left): self.animation_index = 0
            self.image = self.set_image(self.animation_index)

    def apply_walking(self):
        KEYS = pygame.key.get_pressed()
        # jumping
        if KEYS[pygame.K_SPACE] and self.rect.bottom >= 340: self.gravity = -20
        if KEYS[pygame.K_UP] and self.rect.bottom >= 340: self.gravity = -20
        # walking
        if self.rect.right >= WIDTH: self.rect.right = WIDTH
        if self.rect.left <= 0: self.rect.left = 0
        if KEYS[pygame.K_RIGHT]:
            self.rect.x += 3
            self.facing_right = True
            self.animation = True
        elif KEYS[pygame.K_LEFT]:
            self.rect.x -= 3
            self.facing_right = False
            self.animation = True
        else: self.animation = False

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 350: self.rect.bottom = 350

    def update(self):
        self.apply_gravity()
        self.apply_walking()
        self.animate()
