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
        maze_map = maze.get_map()
        dead_end_cells = [] #give these priority
        other_cells = []
        for i in range(len(maze_map)):
            for j in range(len(maze_map[i])):
                if maze_map[i][j] == " ":
                    surrounding_wall_count = 0
                    if maze_map[i+1][j] in barrier_chars:
                        surrounding_wall_count += 1
                    if maze_map[i-1][j] in barrier_chars:
                        surrounding_wall_count += 1
                    if maze_map[i][j+1] in barrier_chars:
                        surrounding_wall_count += 1
                    if maze_map[i][j-1] in barrier_chars:
                        surrounding_wall_count += 1
                        
                    if surrounding_wall_count == 3: #is a dead end
                        dead_end_cells.append(Goal(j,i))
                    else:
                        other_cells.append(Goal(j,i))
        return dead_end_cells + other_cells

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
        elif search_algorithm == SearchAlgoType.A_STAR_VS_GREEDY:
            return GoalFactory.generate_goals_in_all_cells(maze)
        else:
            if maze_size == MazeSize.SMALL:
                return [Goal(14,4)]

            elif maze_size == MazeSize.MEDIUM:
                return [Goal(14,10)]

            elif maze_size == MazeSize.LARGE:
                return [Goal(22,10)]