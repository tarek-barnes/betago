# Attempt at encoding game states as classes, deprecated

import numpy as np

class Stone:
    # Do I need to error if a stone initializes outside goban?
    def __init__(self, location, color):
        self.location = location
        self.color = color

    def on_goban(self, location):
        (x,y) = location
        return ((x>0 and x<20) and (y>0 and y<20))

    def get_neighbors(self):
        (x,y) = self.location
        naive_neighbors = [(x-1, y), (x+1, y),
                           (x, y-1), (x, y+1)]

        return [k for k in naive_neighbors if self.on_goban(k)]


class Goban:
    def __init__(self):
        self.next = "W"
        self.state = np.array([ [0]*19 ] * 19)

    def get_state(self):
        return self.state

    def on_goban2(self, location):
        (x,y) = location
        return ((x>0 and x<20) and (y>0 and y<20))

    def get_neighbors2(self, n):
        (x,y) = n
        naive_neighbors = [(x-1, y), (x+1, y),
                           (x, y-1), (x, y+1)]

        return [k for k in naive_neighbors if self.on_goban2(k)]

    def get_num_liberties(self, stone):
        (x,y) = stone.location
        neighbors = stone.get_neighbors()
        num_liberties = 0
        for k in neighbors:
            (pos_x, pos_y) = k
            if self.state[pos_x-1][pos_y-1] == 0:
                num_liberties += 1
        return num_liberties

    def is_legal_move(self, location):
        (x,y) = location
        return self.state[x-1][y-1] == 0

    def switch_player(self):
        if self.next == "B":
            self.next = "W"
        else:
            self.next = "B"

    def play_stone(self, stone):
        # check if next move is stone color
        # check if location is open/legal
        (x,y) = stone.location
        # can i make this prettier?
        if stone.color == "B":
            self.state[x-1][y-1] = 1
        elif stone.color == "W":
            self.state[x-1][y-1] = 2
        # change next

    def remove_stone(self, stone):
        (x,y) = stone.location
        self.state[x-1][y-1] = 0

    def get_stone_number(self, color):
        if self.color == "B":
            return 1
        elif self.color == "W":
            return 2

    def find_dead_stones(self, stone):
        def go(n):
            (x,y) = n
            visited = []
            visited.append(n)
            new_neighbors = get_neighbors2(n)
            for new_neighbor in new_neighbors:
                if (new_neighbor not in visited) and ():




        neighbors = stone.get_neighbors()
        stone_number = self.get_stone_number(stone.color)

        for neighbor in neighbors:
            (x,y) = neighbor
            if (self.state[x-1][y-1] != 0) and (self.state[x-1][y-1] != stone_number):
                visited = []
                visited.append(neighbor)







# write floodfill
# for a stone that i played, look at its neighbors
# if neighbor is same color, ignore
# if neighbor is diff color, follow the path down:
#  go down the path, and keep a record of visited stones
#  if at the end of the path, you haven't found a liberty, remove all those stones
