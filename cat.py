import pygame
from settings import *

class Cat:
    def __init__(self, image):
        self.image = pygame.transform.scale(image, CAT_SIZE).convert()
        self.rect= self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.speed = 5
        
    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)