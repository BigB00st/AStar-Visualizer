from constants import *
import point
import random


class Maze:
    def __init__(self):
        self.width = MAZE_WIDTH
        self.height = MAZE_HEIGHT
        self.maze = create_maze(self.width, self.height)
        self.start = self.maze[0][0]
        self.start._type = START
        self.end = self.maze[-1][-1]
        self.end._type = END
        self.get_point_neighbors()

    def get_point_neighbors(self):
        for x in range(self.width):
            for y in range(self.height):
                cur = self.maze[x][y]
                if x > 0:
                    cur.neighbors.append(self.maze[x-1][y])
                if x < self.width-1:
                    cur.neighbors.append(self.maze[x+1][y])
                if y > 0:
                    cur.neighbors.append(self.maze[x][y-1])
                if y < self.height-1:
                    cur.neighbors.append(self.maze[x][y+1])

    def draw(self, screen):
        for x in range(MAZE_WIDTH):
            for y in range(MAZE_HEIGHT):
                self.maze[x][y].draw(screen)

    def is_start_or_end(self, p):
        return p == self.end or p == self.start


def create_maze(width, height):
    maze = []
    for x in range(width):
        row = []
        for y in range(height):
            cur = point.Point(x, y)
            if random.randint(0, 100) < OBSTACLE_CHANCE:
                cur._type = OBSTACLE
            row.append(cur)
        maze.append(row)

    return maze


