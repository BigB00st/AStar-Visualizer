import pygame
from constants import *
import maze
import AStar
import time


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("A* Visualizer")


def wait_for_event(_event):
    while True:
        for event in pygame.event.get():
            if event.type == _event:
                return


def main():

    screen.fill(BLANK_COLOR)

    game_maze = maze.Maze()
    game_maze.draw(screen)
    draw_queue = []
    path = AStar.a_star(game_maze.start, game_maze.end, draw_queue)

    if path is None:
        print("Path not found")
        exit()

    pygame.display.flip()

    wait_for_event(pygame.KEYDOWN)

    # draw steps progressively
    for cur_point in draw_queue:
        if not game_maze.is_start_or_end(cur_point):
            cur_point.draw(screen)
            time.sleep(STEP_SLEEP_TIME)
            pygame.display.flip()

    # draw path progressively
    for cur_point in path:
        if not game_maze.is_start_or_end(cur_point):
            cur_point._type = PATH
            cur_point.draw(screen)
            time.sleep(PATH_SLEEP_TIME)
            pygame.display.flip()

    # draw blank nodes with highlight color
    for x in range(game_maze.width):
        for y in range(game_maze.height):
            if game_maze.maze[x][y].get_type() == BLANK:
                game_maze.maze[x][y].set_type(HIGHLIGHT)
                game_maze.maze[x][y].draw(screen)
    pygame.display.flip()

    wait_for_event(pygame.QUIT)


if __name__ == "__main__":
    main()
