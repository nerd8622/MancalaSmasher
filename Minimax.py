import numpy as np


class positionTree:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

    def add(self, child):
        self.children.append(positionTree(self))


def genTree(game, depth):
    pass


def makeDecision(tree):
    pass
