import pygame
import random
import sys
import os
from settings import *
from cat import *
from cheese import *
from messages import *
from obstacle import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load("images/background.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
bg_x = 0  
bg_speed = 1 

cat = Cat(pygame.image.load("images/cat.png"))

planet = Obstacle("images")
        
cheese = Cheese(pygame.image.load("images/cheese.png"))

score = 0

speed = 5

game_over = False

while True:
    bg_x -= bg_speed

    if bg_x <= -WIDTH:
        bg_x = 0

    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + WIDTH, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    cat.move(keys)
    
    if not game_over:
        planet.add_obstacle()  
        game_over=planet.move_obstacles(speed, screen, cat.rect, game_over)

        cheese.add_cheese()  
        score+=cheese.move_cheese(screen, speed, cat.rect)

    cat.draw(screen)  

    show_score(score,screen)
    if game_over:
        (score, game_over) =  finish(keys, planet.obstacles, cheese.cheeses, score, game_over, screen)

    pygame.display.flip()
    clock.tick(60)
