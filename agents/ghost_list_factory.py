"""
Factory class for creating a ghosts for a world
"""
from agents.Ghost import Ghost
from enums.search_algorithm_type import SearchAlgoType
from enums.size import MazeSize

"""
Gets the list of ghosts for a maze based on maze size and search algorithm type
"""
class GhostListFactory:
    @staticmethod
    def get_ghost_list(maze, search_algorithm_enum):
        maze_size = maze.get_maze_size()
        if maze_size == MazeSize.SMALL and search_algorithm_enum == SearchAlgoType.UNIFORM:
            ghost1 = Ghost(5,4)
            return [ghost1]

        elif maze_size == MazeSize.MEDIUM and search_algorithm_enum == SearchAlgoType.UNIFORM:
            ghost1 = Ghost(13,1)
            ghost2 = Ghost(4,14)
            return [ghost1, ghost2]

        elif maze_size == MazeSize.LARGE and search_algorithm_enum == SearchAlgoType.UNIFORM:
            ghost1 = Ghost(5,4)
            ghost2 = Ghost(22,9)
            ghost3 = Ghost(4,14)
            return [ghost1, ghost2, ghost3]

        return []