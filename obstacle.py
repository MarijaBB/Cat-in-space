import pygame
from settings import *
import random
import os

class Obstacle:
    def __init__(self, folder_name):
        self.images = []
        
        directory = os.fsencode(folder_name)
            
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.startswith("planet"): 
                planet_image = pygame.image.load(f"assets/images/{filename}")
                planet_image = pygame.transform.scale(planet_image, OBSTACLE_SIZE)
                self.images.append(planet_image)
        self.timer = 0
        self.obstacles = []
        self.sound = pygame.mixer.Sound("assets/sounds/Nudge.ogg")

    def add(self):
        self.timer += 1
        if self.timer > 120:
            self.timer = 0
            y_pos = random.randint(OBSTACLE_SIZE[0], HEIGHT - OBSTACLE_SIZE[0])

            planet_image = random.choice(self.images)
            rect = planet_image.get_rect()
            rect.topleft = (WIDTH, y_pos)

            self.obstacles.append((planet_image, rect))
        
    def move(self, speed, screen, cat_rect, game_over):
        for image, obs in self.obstacles[:]:
            obs.x -= speed
            screen.blit(image, obs)

            if obs.colliderect(cat_rect):
                self.sound.play()
                game_over = True
            if obs.right < 0:
                self.obstacles.remove((image, obs))
        return game_over