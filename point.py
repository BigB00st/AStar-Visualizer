from constants import *
import pygame


class Point:
    def __init__(self, x, y, _type=BLANK):
        self.loc = (x, y)
        self._type = _type
        self.neighbors = []
        self.cost = 0
        self.estimated_cost = 0
        self.parent = None

    def get_type(self):
        return self._type

    def set_type(self, val):
        self._type = val

    def get_x(self):
        return self.loc[0]

    def get_y(self):
        return self.loc[1]

    def __eq__(self, other):
        return self.get_x() == other.get_x() \
            and self.get_y() == other.get_y()

    def __lt__(self, other):
        return self.estimated_cost < other.estimated_cost

    def __repr__(self):
        return str(self.loc)

    def draw(self, screen):
        location = list(self.loc)
        location[0] *= BLOCK_WIDTH
        location[1] *= BLOCK_HEIGHT
        location.append(BLOCK_WIDTH)
        location.append(BLOCK_HEIGHT)
        pygame.draw.rect(screen, COLORS_DICT[self._type], location)
