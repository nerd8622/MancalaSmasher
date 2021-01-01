# Base game class containing flow of the game

import numpy as np

class Game:
    def __init__(self, avalanche=False):
        self.board = np.empty([2, 6], dtype=int)
        self.board.fill(4)
        self.turn = 0  # player 0 moves then player 1
        self.avalanche = avalanche

    def __repr__(self):
        # make prettier...
        return str(self.board)

    def move(self, column):
        if self.avalanche:
            # avalanche move
            pass
        else:
            # regular move
            pass

