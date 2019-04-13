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
        for event in pygame.event.get():  # User did something
            if event.type == _event:  # If user clicked close
                return


def main():

    screen.fill(BLANK_COLOR)
    game_maze = maze.Maze()
    game_maze.draw(screen)
    draw_queue = []
    path = AStar.a_star(game_maze.start, game_maze.end, draw_queue)

    if len(path) == 0:
        print("Path not found")
        exit()

    pygame.display.flip()

    wait_for_event(pygame.KEYDOWN)

    for cur_point in draw_queue:
        cur_point.draw(screen)
        time.sleep(0.02)
        pygame.display.flip()
    for cur_point in path:
        cur_point._type = PATH
        cur_point.draw(screen)
        time.sleep(0.005)
        pygame.display.flip()

    wait_for_event(pygame.QUIT)


if __name__ == "__main__":
    main()
