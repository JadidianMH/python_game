import pygame
import os
import data

pygame.init()
pygame.font.init()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FONT_PATH = os.path.join(BASE_DIR, 'asset', 'font', 'home.ttf')
scoreFont = pygame.font.Font(FONT_PATH, 20)
titleFont = pygame.font.Font(FONT_PATH, 30)

black        = (30, 30, 30)
white        = (220, 220, 220)
red          = (220, 30, 30)
uiBackground = (0, 0, 0)

gameVersion = data.version

ICON_PATH = os.path.join(BASE_DIR, 'asset', 'image', 'icon.png')
icon = pygame.image.load(ICON_PATH)