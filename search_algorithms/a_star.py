from enums.search_algorithm_type import SearchAlgoType
from search_algorithms.Search_algo import SearchAlgorithm
from search_algorithms.manhattan_distance import ManhattanDistance

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
    def search(self, start_x, start_y, opponent_locations):

        return None
    
    def get_cost(self, location, opponent_locations):
        pass

    def calculate_distance(self, x, y):
        pass
    
    def set_heuristic(self, heuristic):
        self.heuristic = heuristic
        
    def get_enum(self):
        return SearchAlgoType.A_STAR