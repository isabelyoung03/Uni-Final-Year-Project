"""
Factory class for creating a goal for the world
"""
from enums.size import MazeSize
from environment.Goal import Goal

"""
Gets the goal for the maze
"""
class GoalFactory:
    @staticmethod
    def get_goal(maze):
        maze_size = maze.get_maze_size()
        if maze_size == MazeSize.SMALL:
            return Goal(14,4)

        elif maze_size == MazeSize.MEDIUM:
            return Goal(15,6)

        elif maze_size == MazeSize.LARGE:
            return Goal(20,8)