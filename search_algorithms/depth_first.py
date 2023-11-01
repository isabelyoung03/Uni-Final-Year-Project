from enums.search_algorithm_type import SearchAlgoType
from search_algorithms.Search_algo import SearchAlgorithm

"""
Depth-first search
"""
class DepthFirstSearch(SearchAlgorithm):
    def __init__(self, maze, goals):
        self.maze = maze
        self.goal = goals[0]
        self.y_axis_length = len(maze.map)
        self.x_axis_length = len(maze.map[0])

    """
    Searches the maze and returns a path to the goal
    """
    def search(self, start_x, start_y, opponent_locations, path=None) -> list:
        if path is None:
            path = []

        if (start_x, start_y) in path:
            return None #been here before so no solution
        
        if (start_x, start_y) == self.goal.get_location():
            path.append((start_x, start_y))
            return path #goal has been found

        path.append((start_x, start_y))

        for i, j in SearchAlgorithm.movements:
            new_x = start_x + i
            new_y = start_y + j
            if self.maze.check_valid_location(new_x, new_y) and 0 <= new_y < self.y_axis_length and 0 <= new_x < self.x_axis_length:
                result = self.search(new_x, new_y, opponent_locations, path)
                if result:
                    return result
        path.pop()        
        return [] #if no solution found

    def get_enum(self) -> SearchAlgoType:
        return SearchAlgoType.DEPTH
