import pygame
import core.loader as loader
import core.function as function

# === Initialization ===
pygame.init()

# === Window Setup ===

screen, WINDOW_SIZE = function.window_setup()

# === Game Variables ===
clock = pygame.time.Clock()
normalTickRate = 10
tickRate = 5
screenshut = False
slow = True

# === Timer Setup ===
startTick = function.starter_tick()

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 20
snake_velocity = [SNAKE_SPEED, 0]
snake = [[WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2] * 10]

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

# === Ground Generation ===
Ground = function.generate_checkered_ground(SNAKE_SIZE, WINDOW_SIZE[0], WINDOW_SIZE[1])

# === Main Loop ===
running = True

while running:
    screen.fill(loader.black)

    # === Event Handling ===
    result = function.Controller(state, snake_velocity, SNAKE_SPEED, screenshut, WINDOW_SIZE)
    if result[0] == "quit":
        running = False
        continue
    else:
        state, snake_velocity, screenshut = result

    # --- Handle state (pause/game over) ---
    state, snake, tickRate, startTick, skip = function.handle_state(
        screen, state, loader, WINDOW_SIZE, clock, snake, SNAKE_SPEED, apple, tickRate, startTick
    )
    if skip:
        continue


    # === Apple Spawn ===

    function.apple_spawn(apple, SNAKE_SIZE, WINDOW_SIZE, snake)


    # === Snake Movement ===
    new_head = [
        snake[-1][0] + snake_velocity[0],
        snake[-1][1] + snake_velocity[1]
    ]
    snake.append(new_head)

    # === Wall Collision And Self-Kill ===
    if snake[-1][0] < 0 or snake[-1][0] >= WINDOW_SIZE[0] or \
       snake[-1][1] < 0 or snake[-1][1] >= WINDOW_SIZE[1] or \
       snake[-1] in snake[:-1]:
        function.die(snake, screen)
        state = STATE_GAMEOVER
        continue

    # === Apple Collision ===
    if apple["available"] and new_head == apple["pos"]:
        tickRate += .1
        apple["available"] = False
    else:
        snake.pop(0)

    # === Drawing ===
    for tile in Ground:
        x, y = tile
        grid_x = x // SNAKE_SIZE
        grid_y = y // SNAKE_SIZE

        if (grid_x + grid_y) % 2 == 0:
            tileColor = loader.lightGreen
        else:
            tileColor = loader.green

        function.draw_object([SNAKE_SIZE, SNAKE_SIZE], tile, screen, tileColor, False)

    function.draw_object([WINDOW_SIZE[0], 30], [0, WINDOW_SIZE[1]], screen, loader.uiBackground, loader.blank)
    function.draw_text(screen, str(len(snake)), [15, WINDOW_SIZE[1] + 10], loader.white, 15, 2)
    function.draw_text(screen, str(int(tickRate)), [WINDOW_SIZE[0] - 40, WINDOW_SIZE[1] + 10], loader.white, 15, 2)
    if apple["available"]:
        function.draw_object([SNAKE_SIZE, SNAKE_SIZE], apple["pos"], screen, loader.red, loader.shadow)
    function.draw_objects(SNAKE_SIZE, snake, screen, loader.violet, loader.shadow)
    pygame.display.update()
    clock.tick(tickRate)

    if pygame.time.get_ticks() - startTick > 3000 and slow:
        tickRate = normalTickRate
        slow = False

    if screenshut:
        screenshut = False
        function.save_screenshot(screen)

pygame.quit()