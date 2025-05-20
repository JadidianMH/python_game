import pygame
import time

def draw_objects(Size, List, screen, color, shadow):
    for x in List:
        pygame.draw.rect(screen, shadow, [x[0] - 5, x[1] + 5, Size, Size])
    for x in List:
        pygame.draw.rect(screen, color, [x[0], x[1], Size, Size])

def draw_object(Size, pos, screen, color, shadow):
    pygame.draw.rect(screen, shadow, [pos[0] - 5, pos[1] + 5, Size[0], Size[1]])
    pygame.draw.rect(screen, color, [pos[0], pos[1], Size[0], Size[1]])

def starter_tick():
    global slow
    slow = True
    return pygame.time.get_ticks()

def save_screenshot(screen):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    pygame.image.save(screen, f"screenshot_{timestamp}.png")
    print(f"screenshot was saved: screenshot_{timestamp}.png")

pixel_font_5x5 = {
    'A': [
        "01110",
        "10001",
        "11111",
        "10001",
        "10001",
    ],
    'B': [
        "11110",
        "10001",
        "11110",
        "10001",
        "11110",
    ],
    'C': [
        "01111",
        "10000",
        "10000",
        "10000",
        "01111",
    ],
    'D': [
        "11110",
        "10001",
        "10001",
        "10001",
        "11110",
    ],
    'E': [
        "11111",
        "10000",
        "11110",
        "10000",
        "11111",
    ],
    'F': [
        "11111",
        "10000",
        "11110",
        "10000",
        "10000",
    ],
    'G': [
        "01111",
        "10000",
        "10111",
        "10001",
        "01111",
    ],
    'H': [
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
    ],
    'I': [
        "01110",
        "00100",
        "00100",
        "00100",
        "01110",
    ],
    'J': [
        "00111",
        "00010",
        "00010",
        "10010",
        "01100",
    ],
    'K': [
        "10001",
        "10010",
        "11100",
        "10010",
        "10001",
    ],
    'L': [
        "10000",
        "10000",
        "10000",
        "10000",
        "11111",
    ],
    'M': [
        "10001",
        "11011",
        "10101",
        "10001",
        "10001",
    ],
    'N': [
        "10001",
        "11001",
        "10101",
        "10011",
        "10001",
    ],
    'O': [
        "01110",
        "10001",
        "10001",
        "10001",
        "01110",
    ],
    'P': [
        "11110",
        "10001",
        "11110",
        "10000",
        "10000",
    ],
    'Q': [
        "01110",
        "10001",
        "10001",
        "10011",
        "01111",
    ],
    'R': [
        "11110",
        "10001",
        "11110",
        "10010",
        "10001",
    ],
    'S': [
        "01111",
        "10000",
        "01110",
        "00001",
        "11110",
    ],
    'T': [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
    ],
    'U': [
        "10001",
        "10001",
        "10001",
        "10001",
        "01110",
    ],
    'V': [
        "10001",
        "10001",
        "10001",
        "01010",
        "00100",
    ],
    'W': [
        "10001",
        "10001",
        "10101",
        "11011",
        "10001",
    ],
    'X': [
        "10001",
        "01010",
        "00100",
        "01010",
        "10001",
    ],
    'Y': [
        "10001",
        "01010",
        "00100",
        "00100",
        "00100",
    ],
    'Z': [
        "11111",
        "00010",
        "00100",
        "01000",
        "11111",
    ],
    '.': [
        "00000",
        "00000",
        "00000",
        "00000",
        "10000",
    ],
    ':' : [
        "00000",
        "00000",
        "10000",
        "00000",
        "10000",
    ],
    '0': [
        "01110",
        "10011",
        "10101",
        "11001",
        "01110",
    ],
    '1': [
        "00100",
        "01100",
        "00100",
        "00100",
        "01110",
    ],
    '2': [
        "01110",
        "10001",
        "00010",
        "00100",
        "11111",
    ],
    '3': [
        "11110",
        "00001",
        "01110",
        "00001",
        "11110",
    ],
    '4': [
        "10010",
        "10010",
        "11111",
        "00010",
        "00010",
    ],
    '5': [
        "11111",
        "10000",
        "11110",
        "00001",
        "11110",
    ],
    '6': [
        "01110",
        "10000",
        "11110",
        "10001",
        "01110",
    ],
    '7': [
        "11111",
        "00001",
        "00010",
        "00100",
        "01000",
    ],
    '8': [
        "01110",
        "10001",
        "01110",
        "10001",
        "01110",
    ],
    '9': [
        "01110",
        "10001",
        "01111",
        "00001",
        "01110",
    ],
}

def draw_char(screen, ch, pos, color, size=22):
    ch = ch.upper()
    if ch not in pixel_font_5x5:
        return  # skip unsupported characters
    font = pixel_font_5x5[ch]

    pixel_size = max(1, size // 6)
    for y, row in enumerate(font):
        for x, bit in enumerate(row):
            if bit == '1':
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        pos[0] + x * pixel_size,
                        pos[1] + y * pixel_size,
                        pixel_size,
                        pixel_size
                    )
                )

def draw_text(screen, text, pos, color, size=22, spacing=4):
    x, y = pos
    for ch in text:
        if ch == ' ':
            x += size // 2
        else:
            draw_char(screen, ch, (x, y), color, size)
            x += size + spacing

def get_text_width(text, size=22, spacing=2):
    return len(text) * (size + spacing) - spacing