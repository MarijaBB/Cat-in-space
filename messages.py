import pygame
from settings import *

def draw_text(text, x, y, screen, color=WHITE):
    font = pygame.font.SysFont(None, 40)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def show_score(score, screen):
    draw_text(f"Score: {score}", 10, 10, screen)

def finish(keys, obstacles, cheeses, score, game_over, screen):
    draw_text("Game Over! Press R to Restart", WIDTH // 2 - 150, HEIGHT // 2, screen)
    if keys[pygame.K_r]:
        obstacles.clear()
        cheeses.clear()
        score = 0
        game_over = False
    return (score, game_over)
        