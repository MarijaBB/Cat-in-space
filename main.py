import pygame
import random
import sys
import os
from settings import *
from cat import *
from cheese import *
from messages import *
from obstacle import *
from background import *
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = Background(pygame.image.load("images/background.jpg").convert())
cat = Cat(pygame.image.load("images/cat.png"))

planet = Obstacle("images")
        
cheese = Cheese(pygame.image.load("images/cheese.png"))

score = 0

speed = 5

game_over = False

while True:
    background.show_and_move(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    cat.move(keys)
    
    if not game_over:
        planet.add()  
        game_over=planet.move(speed, screen, cat.rect, game_over)

        cheese.add()  
        score += cheese.move(screen, speed, cat.rect)

    cat.draw(screen)  

    show_score(score,screen)
    
    if game_over:
        (score, game_over) =  finish(keys, planet.obstacles, cheese.cheeses, score, game_over, screen)

    pygame.display.flip()
    clock.tick(60)
