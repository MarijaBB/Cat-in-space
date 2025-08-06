import pygame
from settings import *
import random

class Cheese:
    def __init__(self, image):
        self.image = pygame.transform.scale(image, CHEESE_SIZE)
        self.timer = 0
        self.cheeses = []
        self.rect = self.image.get_rect()
        
    def add_cheese(self):         
        self.timer += 1
        if self.timer > 100:
            self.timer = 0
            y_pos = random.randint(0, HEIGHT - CHEESE_SIZE[0] - 10)
            self.rect.center = (WIDTH, y_pos)
            self.cheeses.append(self.rect)
            
    def move_cheese(self, screen, speed, cat_rect) -> int:
        for ch in self.cheeses[:]:
            ch.x -= speed
            screen.blit(self.image, ch)  
            if ch.colliderect(cat_rect):
                self.cheeses.remove(ch)
                return 1
            if ch.right < 0:
                self.cheeses.remove(ch)
        return 0
    
    