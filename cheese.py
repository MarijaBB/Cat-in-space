import pygame
from settings import *
import random

class Cheese:
    def __init__(self, image):
        self.image = pygame.transform.scale(image, CHEESE_SIZE)
        self.timer = 0
        self.cheeses = []
        self.sound = pygame.mixer.Sound(EAT_SOUND)
        
    def add(self):         
        self.timer += 1
        if self.timer > 100:
            self.timer = 0
            y_pos = random.randint(CHEESE_SIZE[0], HEIGHT - CHEESE_SIZE[0])
            rect = self.image.get_rect()
            rect.topleft = (WIDTH, y_pos)
            
            self.cheeses.append((self.image, rect))
       
    def move(self, screen, speed, cat_rect) -> int:
        point_for_collision = 0
        flag = False
        for image, ch in self.cheeses[:]:
            ch.x -= speed
            screen.blit(image, ch)  
            if ch.colliderect(cat_rect):
                self.sound.play()
                self.cheeses.remove((image, ch))
                point_for_collision += 1
                flag = True
            if ch.right < 0:
                self.cheeses.remove((image, ch))
        return point_for_collision, flag

    