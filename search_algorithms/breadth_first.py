from collections import deque
from enums.search_algorithm_type import SearchAlgoType
from search_algorithms.Search_algo import SearchAlgorithm

"""
Breadth-first search 
"""
class BreadthFirstSearch(SearchAlgorithm):
    def __init__(self, maze):
        self.maze = maze
        self.y_axis_length = len(maze.map)
        self.x_axis_length = len(maze.map[0])

    """
    Searches the maze and returns a path to the goal
    """
    def search(self, start_x, start_y):
        queue = deque()
        queue.append([(start_x, start_y)])

        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if self.maze.map[x][y] == 'G':
                return path #goal has been found
            
            for i, j in SearchAlgorithm.movements: #for each possible next square
                new_row = x + i
                new_col = y + j
                if self.maze.check_valid_location(new_row,new_col) and 0 <= new_row < self.y_axis_length and 0 <= new_col < self.x_axis_length:
                    if (new_row, new_col) not in path:
                        new_path = list(path)
                        new_path.append((new_row, new_col))
                        queue.append(new_path)

        return [] #if no solution found
    
    def get_enum(self):
        return SearchAlgoType.BREADTH
