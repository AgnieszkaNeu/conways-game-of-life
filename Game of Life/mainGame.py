import pygame
import random
from button import ButtonImage
from gameOfLife import Individual, Game
import os


WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
SPEED = 10

#Grid
CELL_SIZE = 25
DIMENSION = 30
START_GRID = 10

#Buttons position
IMAGE_POS_X = 800
IMAGE_POS_Y = 40
SPACE_BETWEEN_BUTTONS = 100


#Colors
BACKGROUND_COLOR = (20, 18, 36)
GRID_COLOR =(71, 71, 71)
CELL_COLOR = (255, 255, 255)

#Images
path = os.path.dirname(os.path.abspath(__file__))
start_image = pygame.image.load( path + "\\buttons\\START.png")
stop_image = pygame.image.load( path + "\\buttons\\STOP.png")
random_image = pygame.image.load( path + "\\buttons\\RANDOM.png")
clear_image = pygame.image.load( path + "\\buttons\\CLEAR.png")




def draw_grid(surface):

    for row in range(DIMENSION):
        for col in range(DIMENSION):
            if grid[row][col].is_alive:
                pygame.draw.rect(surface,CELL_COLOR, grid[row][col].rect)
            pygame.draw.rect(surface, GRID_COLOR, grid[row][col].rect, 1)


def initialize_grid(random_distribution=False):
    global grid
    
    for row in range(DIMENSION):
        for col in range(DIMENSION):

            rect = pygame.Rect(col*CELL_SIZE + START_GRID, 
                                    row*CELL_SIZE + START_GRID,
                                    CELL_SIZE,CELL_SIZE)
            
            if random_distribution:
                random_state = random.choices([True,False], weights=[1,10])[0]
                individual = Individual(random_state,row,col,rect)
            else:
                individual = Individual(False,row,col,rect)

            grid[row][col] = individual


def is_within_grid(mouse_pos):
    stop_grid = DIMENSION * CELL_SIZE + START_GRID  
    return (START_GRID <= mouse_pos[0] <= stop_grid) and (START_GRID <= mouse_pos[1] <= stop_grid) 


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
grid = [[0 for x in range(DIMENSION)] for y in range(DIMENSION)]

start_stop_button = ButtonImage(start_image,IMAGE_POS_X,IMAGE_POS_Y,1)
start_stop_button.set_state("start")
random_game_button = ButtonImage( random_image,IMAGE_POS_X, IMAGE_POS_Y+SPACE_BETWEEN_BUTTONS, 1)
clear_button = ButtonImage( clear_image, IMAGE_POS_X, IMAGE_POS_Y+2*SPACE_BETWEEN_BUTTONS, 1)

game = Game(DIMENSION)
pygame.init()
initialize_grid()


while running:

    if start_stop_button.state == "stop":
        game.check_next_states(grid)
        game.update_states(grid)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()

            if start_stop_button.rect.collidepoint(mouse_pos):

                if start_stop_button.state == "start":
                    start_stop_button.set_state("stop", stop_image)
                elif start_stop_button.state == "stop":
                    start_stop_button.set_state("start", start_image)  

            elif random_game_button.rect.collidepoint(mouse_pos):
                initialize_grid(random_distribution = True)

            elif clear_button.rect.collidepoint(mouse_pos):
                initialize_grid()

            elif  is_within_grid(mouse_pos):
                x = (mouse_pos[0] - 10) // CELL_SIZE
                y = (mouse_pos[1] - 10) // CELL_SIZE
                if grid[y][x].rect.collidepoint(mouse_pos):
                    grid[y][x].is_alive = not grid[y][x].is_alive


    ### Draw components
    screen.fill(BACKGROUND_COLOR)
    draw_grid(screen) 
    start_stop_button.draw_button(screen)
    random_game_button.draw_button(screen)
    clear_button.draw_button(screen)

    pygame.display.flip()
    clock.tick(SPEED)  

pygame.quit()