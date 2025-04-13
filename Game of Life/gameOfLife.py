import globals


class Individual:
    def __init__(self,is_alive,x,y):
        self.is_alive = is_alive
        self.x = x
        self.y = y

    def set_next_state(self, is_alive):
        self.next_state = is_alive

    def update_state(self):
        self.is_alive = self.next_state


def check_neighbours(individual,grid):

    neighbours = []
    for x in range(individual.x - 1, individual.x + 2):
        for y in range (individual.y - 1,individual.y + 2):

            if (individual.x == x and individual.y == y) or x<0 or y<0 or x>=globals.DIMENSION or y>=globals.DIMENSION:
                continue
            neighbour = grid[x][y]
            neighbours.append(neighbour.is_alive)
    
    alive_neighbours = neighbours.count(True)
    if alive_neighbours == 3: individual.set_next_state(True)
    elif (alive_neighbours == 3 or alive_neighbours == 2): individual.set_next_state(individual.is_alive)
    else: individual.set_next_state(False)