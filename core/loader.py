import pygame
import os
import data

pygame.init()
pygame.font.init()

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# common variables
scoreFont = pygame.font.SysFont('Home Video', 20)
titleFont = pygame.font.SysFont('Home Video', 30)
black        = ( 30, 30, 30)
white        = (220,220,220)
red          = (220, 30, 30)
uiBackground = (0, 0, 0)

gameVersion = data.version

# images
icon = pygame.image.load(os.path.join(BASE_PATH, '..', 'asset', 'image', 'icon.png'))