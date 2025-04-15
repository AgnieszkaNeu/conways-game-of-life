import pygame

class Individual:
    def __init__(self,is_alive,x,y,rect):
        self.is_alive = is_alive
        self.x = x
        self.y = y
        self.rect = rect

    def set_next_state(self, is_alive):
        self.next_state = is_alive

    def update_state(self):
        self.is_alive = self.next_state


class Game:

    def __init__(self,dimension):
        self.dimension = dimension


    def check_next_states(self,grid):
        for row in range(self.dimension):
            for col in range(self.dimension):
                alive_neighbours = self.get_number_of_alive_neighbours(grid[row][col], grid)
                self.change_next_state(alive_neighbours,grid[row][col])


    def get_number_of_alive_neighbours(self,individual,grid):

        neighbours = []
        for x in range(individual.x - 1, individual.x + 2):
            for y in range (individual.y - 1,individual.y + 2):

                if (individual.x == x and individual.y == y) or x<0 or y<0 or x>=self.dimension or y>=self.dimension:
                    continue
                neighbour = grid[x][y]
                neighbours.append(neighbour.is_alive)
        
        return neighbours.count(True)


    def change_next_state(self,count,individual):
        if count == 3: individual.set_next_state(True)
        elif (count == 3 or count == 2): individual.set_next_state(individual.is_alive)
        else: individual.set_next_state(False)


    def update_states(self,grid):
        for row in range(self.dimension):
            for col in range(self.dimension):
                grid[row][col].update_state()