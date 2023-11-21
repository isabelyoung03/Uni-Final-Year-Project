from collections import deque
from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm

"""
Breadth-first search 
"""
class BreadthFirstSearch(SearchAlgorithm):
    def __init__(self, maze, goals):
        self.maze = maze
        self.goal = goals[0]
        self.y_axis_length = len(maze.map)
        self.x_axis_length = len(maze.map[0])

    """
    Searches the maze and returns a path to the goal
    """
    def search(self, start_x, start_y, opponent_locations) -> list:
        queue = deque()
        queue.append([(start_x, start_y)])

        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if (x, y) == self.goal.get_location():
                return path #goal has been found
            
            for i, j in SearchAlgorithm.movements: #for each possible next square
                new_x = x + i
                new_y = y + j
                if self.maze.check_valid_location(new_x, new_y) and 0 <= new_y < self.y_axis_length and 0 <= new_x < self.x_axis_length:
                    if (new_x, new_y) not in path:
                        new_path = list(path)
                        new_path.append((new_x, new_y))
                        queue.append(new_path)

        return [] #if no solution found
    
    """
    Get enum for this search algorithm
    """
    def get_enum(self):
        return SearchAlgoType.BREADTH
