"""
Factory class for creating a goal for the world
"""
from src.enums.search_algorithm_type import SearchAlgoType
from src.enums.size import MazeSize
from src.environment.Goal import Goal

class GoalFactory:
    """
    Creates a list of goals with one in each path cell, with the dead ends at the front of the list
    """
    @staticmethod     
    def generate_goals_in_all_cells(maze) -> list:
        barrier_chars = ['-', 'X', '+', '|']
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maze_map = maze.get_map()
        dead_end_cells = [] #give these priority
        other_cells = []
        for i in range(len(maze_map)):
            for j in range(len(maze_map[i])):
                if maze_map[i][j] == " ":
                    surrounding_wall_count = 0
                    for x, y in neighbours:
                        if maze_map[i+x][j+y] in barrier_chars:
                            surrounding_wall_count += 1
                    if surrounding_wall_count == 3: #is a dead end
                        dead_end_cells.append(Goal(j,i))
                    else:
                        other_cells.append(Goal(j,i))
        return dead_end_cells + other_cells

    """
    Returns the list of goals for a given maze
    """
    @staticmethod
    def get_goals(maze, search_algorithm) -> list[Goal]:
        maze_size = maze.get_maze_size()
        if search_algorithm == SearchAlgoType.A_STAR:
            if maze_size == MazeSize.SMALL:
                return [Goal(1,6), Goal(1,1), Goal(14,6), Goal(14,1)]

            elif maze_size == MazeSize.MEDIUM:
                return [Goal(14,14), Goal(14,1), Goal(1,1), Goal(1,14)]

            elif maze_size == MazeSize.LARGE:
                return [Goal(24,14), Goal(24,1), Goal(1,14), Goal(1,1)]
        elif search_algorithm == SearchAlgoType.A_STAR_ALL_CELLS or search_algorithm == SearchAlgoType.GREEDY or search_algorithm == SearchAlgoType.REFLEX:
            return GoalFactory.generate_goals_in_all_cells(maze)
        else:
            if maze_size == MazeSize.SMALL:
                return [Goal(7,3)]

            elif maze_size == MazeSize.MEDIUM:
                return [Goal(9,11)]

            elif maze_size == MazeSize.LARGE:
                return [Goal(16,7)]