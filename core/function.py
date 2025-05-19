import pygame
import time

def show_score(score, screen, font, color, place):
    scoreText = font.render('score:' + str(score), False, color)
    screen.blit(scoreText, place)

def draw_snake(snakeSize, snakeList, screen, color):
    for x in snakeList:
        pygame.draw.rect(screen, color, [x[0], x[1], snakeSize, snakeSize])

def message(status, size, screen, color, bg, font):
    pygame.draw.rect(screen, bg, [0, 0, size[0], size[1]])
    Message = font.render(status, False, color)
    screen.blit(Message, [size[0] // 2 - Message.get_width() // 2, size[1] // 2 - Message.get_height() // 2])

def draw_apple(appleSize, apple, screen, color):
    pygame.draw.rect(screen, color, [apple["pos"][0], apple["pos"][1], appleSize, appleSize])

def text_objects(text, font, color, place, screen):
    text = font.render(text, False, color)
    screen.blit(text, place)

def starter_tick():
    return pygame.time.get_ticks()

def save_screenshot(screen):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    pygame.image.save(screen, f"screenshot_{timestamp}.png")
    print(f"screenshot was saved: screenshot_{timestamp}.png")