import math
from enums.search_algorithm_type import SearchAlgoType
from search_algorithms.Search_algo import SearchAlgorithm
from search_algorithms.manhattan_distance import ManhattanDistance
from search_algorithms.node import Node

"""
A* search
"""
class AStarSearch(SearchAlgorithm):
    def __init__(self, maze, goals):
        self.maze = maze
        self.goals = goals
        self.heuristic = None
        self.y_axis_length = len(maze.map)
        self.x_axis_length = len(maze.map[0])

    """
    Searches the maze and returns path to goal
    """
    def search(self, start_x: int, start_y: int) -> list:
        open_list = []
        goal_coord = self.goals[0].get_location()
        h = self.heuristic.get_h(start_x, start_y, goal_coord[0], goal_coord[1])
        first_node = Node(start_x, start_y, 0, h, None)
        open_list.append(first_node)
        closed_list = set()

        while open_list:
            q = None
            min_f = math.inf
            for node in open_list:
                f = node.get_g() + node.get_h()
                if f < min_f:
                    min_f = f
                    q = node

            open_list.remove(q)

            for i, j in SearchAlgorithm.movements:
                new_x = q.get_location()[0] + i
                new_y = q.get_location()[1] + j

                if self.maze.check_valid_location(new_x, new_y) and 0 <= new_y < self.y_axis_length and 0 <= new_x < self.x_axis_length:
                    if (new_x, new_y) == goal_coord: #if goal found
                        path = [q.get_location()]
                        while q.get_parent() is not None: #backtrack through this nodes parents to find the path
                            q = q.get_parent()
                            path.append(q.get_location())
                        path.reverse()
                        path.append(goal_coord)
                        return path
                    else:
                        g = q.get_g() + 1
                        h = self.heuristic.get_h(new_x, new_y, goal_coord[0], goal_coord[1])
                        f = g + h

                        if self.exists_in_list(new_x, new_y, open_list, f):
                            continue
                        if self.exists_in_list(new_x, new_y, closed_list, f):
                            continue
                        else: 
                            successor_node = Node(new_x, new_y, g, h, q) # Create a new node and set the parent to q
                            open_list.append(successor_node)

            closed_list.add(q)
        return None

    """
    Check if location is already in given list and compare f values
    """
    def exists_in_list(self, x: int, y: int, node_list: list, f: int):
        if any(node.get_location() == (x, y) for node in node_list):
            existing_node = next(node for node in node_list if node.get_location() == (x, y))
            if existing_node.get_f() < f:
                return True
        return False

    """
    Set heuristic function
    """
    def set_heuristic(self, heuristic) -> None:
        self.heuristic = heuristic

    """
    Get enum for this search algorithm
    """
    def get_enum(self) -> SearchAlgoType:
        return SearchAlgoType.A_STAR