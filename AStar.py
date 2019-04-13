import bisect
import math
import collections
from constants import *

# Result from A*, able to return multiple variables
Result = collections.namedtuple('Result', ['path', 'frontier', 'closed'])


# Heuristic cost methods (Estimated cost to goal)
############

def manhattan_distance(node, goal):
    return abs(node.get_x() - goal.get_x()) + abs(node.get_y() - goal.get_y())


def euclidean_distance(node, goal):
    return math.sqrt((node.get_x() - goal.get_x())**2 + (node.get_y() - goal.get_y())**2)

############


# Cost so far and heuristic cost
def total_cost(node, goal):
    return node.cost + manhattan_distance(node, goal)


# Reconstruct shortest path from start to goal node
def reconstruct_path(node, start):
    path = list()
    path.append(node)
    while node != start:
        node = node.parent
        path.append(node)
    return path


# Calculate shortest path form start to goal
def a_star(start, goal, draw_queue):
    frontier = [start]
    closed = []

    while frontier:
        current = frontier[0]  # Get node with least cost

        # add to draw queue
        current.set_type(STEP)
        draw_queue.append(current)

        if current == goal:
            path = reconstruct_path(current, start)
            return path

        # Remove current from frontier and add it to closed list
        del frontier[0]
        closed.append(current)

        for neighbor in current.neighbors:
            if neighbor.get_type() == OBSTACLE:  # Blocked node
                closed.append(neighbor)
                continue

            if neighbor in closed or neighbor in frontier:
                continue

            neighbor.parent = current
            neighbor.cost = current.cost
            neighbor.estimated_cost = total_cost(neighbor, goal)

            if neighbor not in frontier:
                bisect.insort(frontier, neighbor)  # Adds node in frontier list (Ascending order)

    return None  # return None if a path was not found

