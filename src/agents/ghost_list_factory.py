"""
Factory class for creating a ghosts for a world
"""
from src.agents.Ghost import Ghost
from src.enums.ghost_behaviour import GhostBehaviour
from src.enums.search_algorithm_type import SearchAlgoType
from src.enums.size import MazeSize

"""
Gets the list of ghosts for a maze based on maze size and search algorithm type
"""
class GhostListFactory:
    """
    Returns a list of ghosts for each maze
    """
    @staticmethod
    def get_ghost_list(maze, search_algorithm_enum) -> list:
        maze_size = maze.get_maze_size()
        if maze_size == MazeSize.SMALL and search_algorithm_enum == SearchAlgoType.UNIFORM:
            ghost1 = Ghost(5,4, maze, GhostBehaviour.RANDOM)
            return [ghost1]

        elif maze_size == MazeSize.MEDIUM and search_algorithm_enum == SearchAlgoType.UNIFORM:
            ghost1 = Ghost(10,6, maze, GhostBehaviour.RANDOM)
            ghost2 = Ghost(4,14, maze, GhostBehaviour.RANDOM)
            ghost3 = Ghost(8,8, maze, GhostBehaviour.RANDOM)
            return [ghost1, ghost2, ghost3]

        elif maze_size == MazeSize.LARGE and search_algorithm_enum == SearchAlgoType.UNIFORM:
            ghost1 = Ghost(5,4, maze, GhostBehaviour.RANDOM)
            ghost2 = Ghost(22,2, maze, GhostBehaviour.RANDOM)
            ghost3 = Ghost(4,14, maze, GhostBehaviour.RANDOM)
            ghost4 = Ghost(8,9, maze, GhostBehaviour.RANDOM)
            ghost5 = Ghost(12,5, maze, GhostBehaviour.RANDOM)
            ghost6 = Ghost(15,3, maze, GhostBehaviour.RANDOM)
            return [ghost1, ghost2, ghost3, ghost4, ghost5, ghost6]

        return []