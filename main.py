import pygame
import sys
from settings import *
from cat import *
from cheese import *
from helper_functions import *
from obstacle import *
from background import *
from boss import *
from database.highscore import *

init_database_table()
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = Background(pygame.image.load("assets/images/background.jpg"))

cat = Cat(pygame.image.load("assets/images/cat.png"))

planet = Obstacle("assets/images")
        
cheese = Cheese(pygame.image.load("assets/images/cheese.png"))

dog = Boss(pygame.image.load("assets/images/dog.png"))
score = 0

speed = START_SPEED

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
        if score < BOSS_LEVEL_TRESHOLD:
            planet.add()  
            game_over=planet.move(speed, screen, cat.rect, game_over)

            cheese.add()  
            score += cheese.move(screen, speed, cat.rect)
            if score != 0 and score % 5 == 0:
                speed += ACCELERATION
        if score >= BOSS_LEVEL_TRESHOLD:
            dog.add()
            game_over = dog.move(speed, screen, cat.rect, game_over)
            
    cat.draw(screen)  

    show_score(score,screen)
    
    if game_over:
        (score, game_over) =  finish(keys, planet.obstacles, cheese.cheeses, dog.bosses, score, game_over, screen)
        speed = START_SPEED

    pygame.display.flip()
    clock.tick(100)