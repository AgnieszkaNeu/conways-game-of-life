import pygame
import random
from button import ButtonImage
import globals
import gameOfLife


pygame.init()
screen = pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

grid = [[0 for x in range(globals.DIMENSION)] for y in range(globals.DIMENSION)]


def draw_grid():

    for row in range(globals.DIMENSION):
        for col in range(globals.DIMENSION):

            rect = pygame.Rect(col*globals.CELL_SIZE + globals.START_GRID,
                               row*globals.CELL_SIZE + globals.START_GRID,
                               globals.CELL_SIZE,globals.CELL_SIZE)
            
            if grid[row][col].is_alive:
                pygame.draw.rect(screen,"white",rect)
            pygame.draw.rect(screen, "gray20", rect, 1)


def calculate_next_states():
    for row in range(globals.DIMENSION):
        for col in range(globals.DIMENSION):
            gameOfLife.check_neighbours(grid[row][col], grid)


def update_states():
    for row in range(globals.DIMENSION):
        for col in range(globals.DIMENSION):
            grid[row][col].update_state()


def initialize_grid(random_distribution=False):
    global grid
    
    for row in range(globals.DIMENSION):
        for col in range(globals.DIMENSION):
            if random_distribution:
                random_state = random.choices([True,False], weights=[1,10])[0]
                individual = gameOfLife.Individual(random_state,row,col)
            else:
                individual = gameOfLife.Individual(False,row,col)

            grid[row][col] = individual


start_stop_button = ButtonImage(globals.start_image,500,40,1)
start_stop_button.set_state("stop")

random_game_button = ButtonImage(globals.random_image,500,140,1)

initialize_grid()
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()

            if start_stop_button.rect.collidepoint(mouse_pos):

                if start_stop_button.state == "start":
                    start_stop_button.set_state("stop", globals.stop_image)
                elif start_stop_button.state == "stop":
                    start_stop_button.set_state("start", globals.start_image)  

            if random_game_button.rect.collidepoint(mouse_pos):
                initialize_grid(random_distribution = True)


    screen.fill("black")

    start_stop_button.draw_button(screen)
    random_game_button.draw_button(screen)

    draw_grid()
    calculate_next_states()
    if start_stop_button.state == "start":
        update_states()

    pygame.display.flip()
    clock.tick(globals.SPEED)  

pygame.quit()