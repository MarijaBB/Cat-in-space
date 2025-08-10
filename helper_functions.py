import sys
import pygame
from settings import *
from highscores import *

pygame.font.init()
font = pygame.font.SysFont(None, 40)

def draw_text(text, x, y, screen, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def show_score(score, screen):
    draw_text(f"Score: {score}", 10, 10, screen)

name_entered = False

def finish(keys, obstacles, bosses, cheeses, score, game_over, screen):
    global name_entered

    max_saved_score = get_max_score()
    if game_over and not name_entered and max_saved_score < score: 
        name = get_player_name(screen)
        add_score(name, score)
        name_entered = True
    
    screen.fill((0, 0, 0))
    draw_high_scores(screen)
    draw_text("Game Over! Press R to Restart", WIDTH // 2 - 150, HEIGHT // 2, screen)
    
    if keys[pygame.K_r]:
        obstacles.clear()
        cheeses.clear()
        bosses.clear()
        score = 0
        game_over = False
        name_entered = False
    
    return (score, game_over)

def draw_high_scores(screen):
    scores = get_highscores()
    y = 100 
    for i, row in enumerate(scores):
        text_surface = font.render(f"{i+1}. {row['name']} - {row['score']} ", True, WHITE)
        screen.blit(text_surface, (100, y))
        y += 40 

def get_player_name(screen):
    name = ""
    typing = True
    
    while typing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if name.strip(): 
                        typing = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if event.unicode.isprintable() and len(name) < 20:
                        name += event.unicode
        
        screen.fill((0, 0, 0))
        
        prompt_text = font.render("New high score. Enter your name: ", True, WHITE)
        name_text = font.render(name + "|", True, WHITE)  
        
        screen.blit(prompt_text, (50, 50))
        screen.blit(name_text, (50, 100))
        
        instruction = font.render("Press ENTER when done", True, (200, 200, 200))
        screen.blit(instruction, (50, 150))
        
        pygame.display.flip() 
        
    return name.strip()  


def handle_event_quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()        