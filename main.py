import pygame
import random
import core.loader as loader
import core.function as function
import winsound

# === Initialization ===
pygame.init()

# === Window Setup ===
WINDOW_SIZE = [400, 400]
screen = pygame.display.set_mode([WINDOW_SIZE[0], WINDOW_SIZE[1] + 30])
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(loader.icon)

# === Game Variables ===
clock = pygame.time.Clock()
normalTickRate = 10
tickRate = normalTickRate
screenshut = False

# === Timer Setup ===
startTick = function.starter_tick()

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 20
snake_velocity = [SNAKE_SPEED, 0]
snake = [[WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]]

# Apple properties
apple = {
    "pos": [0, 0],
    "available": False
}

# === Game State ===
STATE_RUNNING = "running"
STATE_PAUSED = "paused"
STATE_GAMEOVER = "gameover"
state = STATE_PAUSED

running = True

while running:
    screen.fill(loader.black)

    # === Event Handling ===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == STATE_RUNNING:
                    winsound.Beep(1000, 500)
                    state = STATE_PAUSED
                elif state == STATE_PAUSED:
                    state = STATE_RUNNING
            if state == STATE_RUNNING:
                if event.key == pygame.K_UP and snake_velocity[1] == 0:
                    snake_velocity = [0, -SNAKE_SPEED]
                elif event.key == pygame.K_DOWN and snake_velocity[1] == 0:
                    snake_velocity = [0, SNAKE_SPEED]
                elif event.key == pygame.K_LEFT and snake_velocity[0] == 0:
                    snake_velocity = [-SNAKE_SPEED, 0]
                elif event.key == pygame.K_RIGHT and snake_velocity[0] == 0:
                    snake_velocity = [SNAKE_SPEED, 0]
                elif event.key == pygame.K_s:
                    screenshut = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                # Left mouse button clicked
                if event.pos[0] < WINDOW_SIZE[0] and event.pos[1] < WINDOW_SIZE[1]:
                    if state == STATE_PAUSED:
                        state = STATE_RUNNING
                    elif state == STATE_RUNNING:
                        state = STATE_PAUSED
            elif event.button == 1 and state == STATE_RUNNING:
                # Right mouse button clicked
                mx, my = event.pos
                cx, cy = WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2
                dx = mx - cx
                dy = my - cy
                if abs(dx) > abs(dy):
                    if dx > 0 and snake_velocity[0] == 0:
                        snake_velocity = [SNAKE_SPEED, 0]
                    elif dx < 0 and snake_velocity[0] == 0:
                        snake_velocity = [-SNAKE_SPEED, 0]
                else:
                    if dy > 0 and snake_velocity[1] == 0:
                        snake_velocity = [0, SNAKE_SPEED]
                    elif dy < 0 and snake_velocity[1] == 0:
                        snake_velocity = [0, -SNAKE_SPEED]

    if state == STATE_PAUSED:
        function.text_objects("game version: " + loader.gameVersion, loader.scoreFont, loader.white, [10, WINDOW_SIZE[1] + 5], screen)
        function.message("Paused", WINDOW_SIZE, screen, loader.white, loader.uiBackground, loader.titleFont)
        pygame.display.update()
        clock.tick(60)
        continue

    if state == STATE_GAMEOVER:
        function.message("Game Over", WINDOW_SIZE, screen, loader.red, loader.black, loader.titleFont)
        pygame.display.update()
        soundLenth = 7
        while soundLenth > 2:
            soundLenth -= 1
            winsound.Beep(int(soundLenth * 120), 190)
        pygame.time.delay(1500)
        # Reset the game
        snake = [[WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]]
        snake_velocity = [SNAKE_SPEED, 0]
        apple["available"] = False
        tickRate = 5
        startTick = function.starter_tick()
        state = STATE_PAUSED
        continue

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

    # === Wall Collision And Self-Kill ===
    if snake[-1][0] < 0 or snake[-1][0] > WINDOW_SIZE[0] or \
       snake[-1][1] < 0 or snake[-1][1] > WINDOW_SIZE[1] or \
       snake[-1] in snake[:-1]:
        state = STATE_GAMEOVER
        continue

    # === Apple Collision ===
    if apple["available"] and new_head == apple["pos"]:
        winsound.Beep(500, 1000)
        apple["available"] = False
    else:
        snake.pop(0)

    # === Drawing ===
    if apple["available"]:
        function.draw_apple(SNAKE_SIZE, apple, screen, loader.red)
    function.draw_snake(SNAKE_SIZE, snake, screen, loader.white)
    pygame.draw.rect(screen, loader.uiBackground, [0, WINDOW_SIZE[1], WINDOW_SIZE[0], 30])
    function.show_score(len(snake) - 1, screen, loader.scoreFont, loader.white, [10, WINDOW_SIZE[1] + 5])
    function.text_objects(str(tickRate), loader.scoreFont, loader.white, [WINDOW_SIZE[0] - 50, WINDOW_SIZE[1] + 5], screen)

    pygame.display.update()
    clock.tick(tickRate)

    if pygame.time.get_ticks() - startTick > 3000:
        tickRate = normalTickRate
    if screenshut:
        screenshut = False
        function.save_screenshot(screen)

pygame.quit()