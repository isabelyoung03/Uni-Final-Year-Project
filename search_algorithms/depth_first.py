from search_algorithms.Search_algo import SearchAlgorithm


class DepthFirstSearch(SearchAlgorithm):
    def __init__(self, maze):
        self.maze = maze
        self.row_count = len(maze.map)
        self.column_count = len(maze.map[0])

    def search(self, start_x, start_y, path=None):
        if path is None:
            path = []

        if (start_x, start_y) in path:
            return None #been here before so no solution
        
        if self.maze.map[start_x][start_y] == 'G':
            return path #goal has been found

        path.append((start_x, start_y))

        for i, j in SearchAlgorithm.movements:
            new_row = start_x + i
            new_col = start_y + j
            if self.maze.check_valid_location(new_row,new_col) and 0 <= new_row < self.row_count and 0 <= new_col < self.column_count:
                result = self.search(new_row, new_col, path)
                if result:
                    return result
        path.pop()        
        return []

        
