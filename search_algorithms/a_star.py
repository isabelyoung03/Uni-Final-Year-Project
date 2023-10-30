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
        self.heuristic = ManhattanDistance
        self.y_axis_length = len(maze.map)
        self.x_axis_length = len(maze.map[0])

    """
    Searches the maze and returns best square to go to next
    """
    def search(self, start_x, start_y):
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

            g = q.get_g() + 1
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
                        return path

                    h = self.heuristic.get_h(new_x, new_y, goal_coord[0], goal_coord[1])
                    successor_node = Node(new_x, new_y, g, h, q) # create new node and set parent to q
                    open_list.append(successor_node)

            closed_list.add(q)
        return None

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    def get_enum(self):
        return SearchAlgoType.A_STAR