import pygame
from settings import *
import random

class Boss:
    def __init__(self, image):
        self.image = pygame.transform.scale(image, BOSS_SIZE)
        self.timer = 0
        self.bosses = []
        self.sound = pygame.mixer.Sound("assets/sounds/Nudge.ogg")
        
    def add(self):         
        self.timer += 1
        if self.timer > 250:
            self.timer = 0
            y_pos = random.randint(50, HEIGHT - BOSS_SIZE[0])
            rect = self.image.get_rect()
            rect.topleft = (WIDTH, y_pos)
            
            self.bosses.append((self.image, rect))
       
    def move(self, speed, screen, cat_rect, game_over) -> int:
        for image, r in self.bosses[:]:
            r.x -= speed
            boss_speed_y = 0.7
            if r.centery < cat_rect.centery:
                r.y += boss_speed_y
            elif r.centery > cat_rect.centery:
                r.y -= boss_speed_y
                
            screen.blit(image, r)  
            if r.colliderect(cat_rect):
                self.sound.play()
                game_over = True
            if r.right < 0:
                self.bosses.remove((image, r))
        return game_over