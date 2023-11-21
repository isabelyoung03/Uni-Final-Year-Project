import math
from queue import PriorityQueue
from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm

"""
Uniform-cost search
"""
class UniformCostSearch(SearchAlgorithm):
    def __init__(self, maze, goals):
        self.maze = maze
        self.goal = goals[0]
        self.y_axis_length = len(maze.map)
        self.x_axis_length = len(maze.map[0])

    """
    Searches the maze and returns path to goal
    """
    def search(self, start_x:int, start_y:int, opponent_locations: list) -> list:
        frontier = PriorityQueue()
        frontier.put((0, [(start_x, start_y)]))  

        while not frontier.empty():
            cost, path = frontier.get()
            x, y = path[-1]  

            if (x, y) == self.goal.get_location(): #if goal found
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
    
    """
    Get the code of going to a location
    """
    def get_cost(self, location, opponent_locations) -> int:
        cost = 1
        min_distance_to_opponent = min(self.calculate_distance(location, opponent) for opponent in opponent_locations)
        if min_distance_to_opponent <= 2: #if near to a ghost
            cost += 9 #increase cost
        return cost

    """
    Calculate distance between two points, x and y for any number of dimensions
    """
    def calculate_distance(self, x:int, y:int) -> int:
        distance = 0
        for i in range(len(x)):
            distance += (x[i] - y[i]) ** 2
        distance = math.sqrt(distance)
        return distance
    
    """
    Get enum for this search algorithm
    """
    def get_enum(self) -> SearchAlgoType:
        return SearchAlgoType.UNIFORM