import pygame
import os

#Constants
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480

#Grid
CELL_SIZE = 10
DIMENSION = 45
START_GRID = 10


#Images
path = os.path.dirname(os.path.abspath(__file__))
start_image = pygame.image.load( path + "\\START.png")
stop_image = pygame.image.load( path + "\\STOP.png")
random_image = pygame.image.load( path + "\\RANDOM.png")


SPEED = 10