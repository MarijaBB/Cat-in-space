import pygame
from settings import *

class Background:
    def __init__(self, image):
        self.image = pygame.transform.scale(image, (WIDTH, HEIGHT))
        self.x = 0  
        self.speed = 1 
       
    def show_and_move(self, screen): 
        self.x -= self.speed

        if self.x <= -WIDTH:
            self.x = 0

        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + WIDTH, 0))