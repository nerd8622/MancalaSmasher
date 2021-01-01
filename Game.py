# Base game class containing flow of the game

import numpy as np

class Game:
    def __init__(self, avalanche=False):
        self.scores = np.zeros([2], dtype=int)
        self.board = np.empty([2, 6], dtype=int)
        self.board.fill(4)
        self.turn = 0  # player 0 moves then player 1
        self.avalanche = avalanche

    def __repr__(self):
        # make prettier...
        return str(self.board)

    def move(self, column):
        marbles = self.board[self.turn, column]
        self.board[self.turn, column] = 0
        dropper = column
        side = self.turn

        if self.avalanche:
            # avalanche move
            pass
        else:
            while marbles:
                dropper += (1 if side else -1)
                if (dropper < 0) or (dropper > 5):  # check for out of bounds
                    if self.turn == side:
                        self.scores[self.turn] += 1
                        marbles -= 1
                        if not marbles:
                            break
                    side = ~side
                    dropper += (1 if side else -1)
                self.board[side, dropper] += 1
                marbles -= 1

        if (dropper < 0) or (dropper > 5):
            pass  # player lands in goal and gets another turn
        else:
            if (self.turn == side) and (self.board[side, dropper] == 1):
                if self.board[~side, dropper]:
                    self.scores[self.turn] += self.board[~side, dropper] + 1
                    self.board[side, dropper] = self.board[~side, dropper] = 0
            self.turn = ~self.turn

    def possibleMoves(self):
        pass
