import math
from queue import PriorityQueue
from enums.search_algorithm_type import SearchAlgoType
from search_algorithms.Search_algo import SearchAlgorithm

"""
Uniform-cost search
"""
class UniformCostSearch(SearchAlgorithm):
    def __init__(self, maze):
        self.maze = maze
        self.y_axis_length = len(maze.map)
        self.x_axis_length = len(maze.map[0])

    """
    Searches the maze and returns best square to go to next
    """
    def search(self, start_x, start_y, opponent_locations):
        frontier = PriorityQueue()
        frontier.put((0, [(start_x, start_y)]))  

        while not frontier.empty():
            cost, path = frontier.get()
            x, y = path[-1]  

            if self.maze.map[y][x] == 'G':
                return path  

            for i, j in SearchAlgorithm.movements:
                new_x = x + i
                new_y = y + j
                if self.maze.check_valid_location(new_x, new_y) and 0 <= new_y < self.y_axis_length and 0 <= new_x < self.x_axis_length:
                    if (new_x, new_y) not in path:
                        new_cost = cost + self.get_cost((new_x, new_y), opponent_locations)
                        new_path = list(path)  
                        new_path.append((new_x, new_y))
                        frontier.put((new_cost, new_path))
        return None
    
    def get_cost(self, location, opponent_locations):
        cost = 1
        min_distance_to_opponent = min(self.calculate_distance(location, opponent) for opponent in opponent_locations)
        if min_distance_to_opponent <= 2: #if near to a ghost
            cost += 9 #increase cost
        return cost

    def calculate_distance(self, x, y):
        distance = 0
        for i in range(len(x)):
            distance += (x[i] - y[i]) ** 2
        distance = math.sqrt(distance)
        return distance
    
    def get_enum(self):
        return SearchAlgoType.UNIFORM