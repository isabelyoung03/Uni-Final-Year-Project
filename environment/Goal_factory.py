"""
Factory class for creating a goal for the world
"""
from enums.search_algorithm_type import SearchAlgoType
from enums.size import MazeSize
from environment.Goal import Goal

"""
Gets the goals for the maze
"""
class GoalFactory:
    @staticmethod
    def get_goals(maze, search_algorithm):
        maze_size = maze.get_maze_size()
        if search_algorithm == SearchAlgoType.A_STAR:
            if maze_size == MazeSize.SMALL:
                return [Goal(14,4)]

            elif maze_size == MazeSize.MEDIUM:
                return [Goal(14,10)]

            elif maze_size == MazeSize.LARGE:
                return [Goal(22,10)]
        else:
            if maze_size == MazeSize.SMALL:
                return [Goal(14,4)]

            elif maze_size == MazeSize.MEDIUM:
                return [Goal(14,10)]

            elif maze_size == MazeSize.LARGE:
                return [Goal(22,10)]