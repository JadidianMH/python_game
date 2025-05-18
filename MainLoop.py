import pygame

pygame.init()

# window
size = [600,800]
pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# neccessary variables
clock = pygame.time.Clock()
running = True

# Snake properties
snakeSize = 20
snakeSpeed = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()