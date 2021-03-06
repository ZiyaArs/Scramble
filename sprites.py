import pygame
from settings import *
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vx = 0
        self.vy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.vy = -5
            if self.rect.y < 0:
                self.rect.y += 5
        if keys[pygame.K_DOWN]:
            self.vy = 5
        if keys[pygame.K_RIGHT]:
            self.vx = 5
            if self.rect.x > (WIDTH-58):
                self.rect.x -= 5
        if keys[pygame.K_LEFT]:
            self.vx = -5
            if self.rect.x < 0:
                self.rect.x += 5

        self.rect.x += self.vx
        self.rect.y += self.vy

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 3))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx = 0

    def update(self):
        keys = pygame.key.get_pressed()

        self.rect.x += self.vx
        if self.rect.x > WIDTH:
            self.kill()
        if keys[pygame.K_SPACE]:
            self.vx = 2
        self.rect.x += self.vx

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.vx = 3
        self.rect.x -= self.vx

class enemyRocket(pygame.sprite.Sprite):
    def __init__(self,x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fly = False
        self.vy = 0

    def update(self):
        self.vx = 3
        self.rect.x -= self.vx
