import pygame
import random
import core.loader as loader
import core.function as function

# === Initialization ===
pygame.init()

# === Window Setup ===
WINDOW_SIZE = [400, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snake Game")

# === Game Variables ===
clock = pygame.time.Clock()
running = True

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 20
snake_velocity = [SNAKE_SPEED, 0]
snake = [[WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]]  # Initial position (center)

# Apple properties
apple = {
    "pos": [0, 0],
    "available": False
}

# === Game Loop ===
while running:
    screen.fill(loader.black)

    # === Event Handling ===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_velocity[1] == 0:
                snake_velocity = [0, -SNAKE_SPEED]
            elif event.key == pygame.K_DOWN and snake_velocity[1] == 0:
                snake_velocity = [0, SNAKE_SPEED]
            elif event.key == pygame.K_LEFT and snake_velocity[0] == 0:
                snake_velocity = [-SNAKE_SPEED, 0]
            elif event.key == pygame.K_RIGHT and snake_velocity[0] == 0:
                snake_velocity = [SNAKE_SPEED, 0]

    # === Apple Spawn ===
    if not apple["available"]:
        apple["pos"] = [
            random.randint(0, WINDOW_SIZE[0] // SNAKE_SIZE - 1) * SNAKE_SIZE,
            random.randint(0, WINDOW_SIZE[1] // SNAKE_SIZE - 1) * SNAKE_SIZE
        ]
        apple["available"] = True
    # === Snake Movement ===
    new_head = [
        snake[-1][0] + snake_velocity[0],
        snake[-1][1] + snake_velocity[1]
    ]
    snake.append(new_head)

    # === Wall Collision ===
    if snake[-1][0] < 0 or snake[-1][0] > WINDOW_SIZE[0] or \
       snake[-1][1] < 0 or snake[-1][1] > WINDOW_SIZE[1]:
        function.message("Game Over", WINDOW_SIZE, screen, loader.red, loader.black, loader.titleFont)
        pygame.display.update()
        pygame.time.delay(3000)

        # Reset the game
        snake = [[WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]]
        snake_velocity = [SNAKE_SPEED, 0]
        apple["available"] = False
        continue
        

    # === Apple Collision ===
    if apple["available"] and new_head == apple["pos"]:
        apple["available"] = False  # Snake eats the apple (grows)
    else:
        snake.pop(0)  # If no apple eaten, remove tail

    # === Drawing ===
    if apple["available"]:
        function.draw_apple(SNAKE_SIZE, apple, screen, loader.red)

    function.draw_snake(SNAKE_SIZE, snake, screen, loader.white)

    pygame.display.update()
    clock.tick(12)

pygame.quit()