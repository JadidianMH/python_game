import pygame
import loader

def show_score(score, screen):
    scoreText = loader.scoreFont.render('score:' + str(score), True, loader.black)
    screen.blit(scoreText, [35, 10])

def draw_snake(snakeSize, snakeList, screen):
    for x in snakeList:
        pygame.draw.rect(screen, loader.white, [x[0], x[1], snakeSize, snakeSize])