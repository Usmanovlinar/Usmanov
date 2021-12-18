import random
from abc import ABC, abstractmethod


class Board:
    SIZE_BOARD = 8
    def __init__(self):
        list_ = [[None for j in range(self.SIZE_BOARD)] for i in range(self.SIZE_BOARD)]

    def generate_figures(self, n):
        for i in range(n-1):
            figure = random.choice([Pawn(random.randint(0,8), random.randint(0,8)),
                                    Rook(random.randint(0,8), random.randint(0,8))
                                    ])
class Figure(ABC):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def attack_position(self):
        pass


class Pawn(Figure):
    def attack_position(self):
        return [(self.x + 1, self.y + 1),
                (self.x - 1, self.y - 1)
                ]


class Rook(Figure):

    def attack_position(self):
        list_= []
        for i in range(8):
            list_.append((self.x + i , self.y))
            list_.append((self.x - i , self.y))
            list_.append((self.x , self.y + i))
            list_.append((self.x , self.y - i))
        return list_

class Bishop(Figure):
    def attack_position(self):
        list_ = []
        for i in range(8):
            list_.append((self.x + i, self.y-i))
            list_.append((self.x -i, self.y+i))
            list_.append((self.x-i, self.y - i))
            list_.append((self.x+i, self.y + i))
        return list_


class Horse(Figure):
    def attack_pozition(self):
        return [(self.x + 2, self.y + 1), (self.x + 2, self.y- 1),
                (self.x - 2, self.y + 1), (self.x - 2,self.y - 1),
                (self.y + 2, self.x + 1), (self.y + 2, self.x - 1),
                (self.y - 2, self.x + 1), (self.y - 2, self.x - 1)]

        return list_

class Queen(Figure):
    def attack_pozition(self):
        list_ = []
        for i in range(8):
            list_.append((self.x + i, self.y))
            list_.append ((self.x - i, self.y))
            list_.append((self.x, self.y + i))
            list_.append ((self.x, self.y - i))
            list_.append((self.x + i, self.y-i))
            list_.append((self.x -i, self.y+i))
            list_.append((self.x-i, self.y - i))
            list_.append((self.x+i, self.y + i))
        return list_

class King(Figure):
    list_ = []
    kingMoves = ((-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1),(1, -1), (1, 0), (1, 1))
    for i in range(8):
        list_.append(())