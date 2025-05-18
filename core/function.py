import pygame

def show_score(score, screen, font, color):
    scoreText = font.render('score:' + str(score), True, color)
    screen.blit(scoreText, [35, 10])

def draw_snake(snakeSize, snakeList, screen, color):
    for x in snakeList:
        pygame.draw.rect(screen, color, [x[0], x[1], snakeSize, snakeSize])

def message(status, size, screen, color, bg, font):
    pygame.draw.rect(screen, bg, [0, 0, size[0], size[1]])
    Message = font.render(status, True, color)
    screen.blit(Message, [size[0] // 2 - Message.get_width() // 2, size[1] // 2 - Message.get_height() // 2])

def draw_apple(appleSize, apple, screen, color):
    pygame.draw.rect(screen, color, [apple["pos"][0], apple["pos"][1], appleSize, appleSize])