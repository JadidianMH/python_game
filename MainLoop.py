import pygame
import core.loader as loader
import core.function as function

pygame.init()

# window
size = [400,400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# neccessary variables
clock = pygame.time.Clock()
running = True
snake = []

# Snake properties
snakeSize = 20
snakeSpeed = 20
snakeVelocity = [snakeSpeed, 0]


snake.append([size[0] // 2, size[1] // 2])

while running:
    screen.fill(loader.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakeVelocity[1] = -snakeSpeed
                snakeVelocity[0] = 0
                print("UP")
            elif event.key == pygame.K_DOWN:
                snakeVelocity[1] = snakeSpeed
                snakeVelocity[0] = 0
                print("DOWN")
            elif event.key == pygame.K_LEFT:
                snakeVelocity[0] = -snakeSpeed
                snakeVelocity[1] = 0
                print("LEFT")
            elif event.key == pygame.K_RIGHT:
                snakeVelocity[0] = snakeSpeed
                snakeVelocity[1] = 0
                print("RIGHT")
        
    snake.append([snake[0][0] + snakeVelocity[0], snake[0][1] + snakeVelocity[1]])
    snake.pop(0)
    function.draw_snake(snakeSize, snake, pygame.display.get_surface(), loader.white)

    pygame.display.update()
    clock.tick(10)
    
pygame.quit()