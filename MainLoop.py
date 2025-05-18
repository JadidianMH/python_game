import pygame
import core.loader as loader
import core.function as function
import random

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

# Apples for the snake
appleSize = snakeSize
apple = {
    "pos": [0, 0],
    "isAvailable": False
}

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

            elif event.key == pygame.K_DOWN:
                snakeVelocity[1] = snakeSpeed
                snakeVelocity[0] = 0

            elif event.key == pygame.K_LEFT:
                snakeVelocity[0] = -snakeSpeed
                snakeVelocity[1] = 0

            elif event.key == pygame.K_RIGHT:
                snakeVelocity[0] = snakeSpeed
                snakeVelocity[1] = 0
    print(len(snake))
    
    ate_apple = False

    if not apple["isAvailable"]:
        randomPos = [random.randint(0, size[0] // appleSize - 1) * appleSize, random.randint(0, size[1] // appleSize - 1) * appleSize]
        apple["pos"] = randomPos
        apple["isAvailable"] = True
        function.draw_snake(appleSize, [apple["pos"]], screen, loader.red)
    else:
        if apple["pos"] == snake[-1]:
            apple["isAvailable"] = False
            ate_apple = True  # Snake will grow
        function.draw_snake(appleSize, [apple["pos"]], screen, loader.red)

    # Move snake
    new_head = [snake[-1][0] + snakeVelocity[0], snake[-1][1] + snakeVelocity[1]]
    snake.append(new_head)
    if not ate_apple:
        snake.pop(0)  # Only remove tail if not eating apple

    function.draw_snake(snakeSize, snake, pygame.display.get_surface(), loader.white)

    pygame.display.update()
    clock.tick(12)
    
pygame.quit()