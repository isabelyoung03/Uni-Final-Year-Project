"""
Factory class for creating a ghosts for a world
"""
from src.agents.MinimaxGhost import MinimaxGhost
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
        behaviour = GhostBehaviour.RANDOM
        if search_algorithm_enum == SearchAlgoType.UNIFORM or search_algorithm_enum == SearchAlgoType.REFLEX:
            if search_algorithm_enum == SearchAlgoType.UNIFORM:
                behaviour = GhostBehaviour.RANDOM_CHASE
            if maze_size == MazeSize.SMALL:
                ghost1 = Ghost(10,5, maze, behaviour)
                return [ghost1]

            elif maze_size == MazeSize.MEDIUM:
                ghost1 = Ghost(10,6, maze, behaviour)
                ghost2 = Ghost(4,14, maze, behaviour)
                ghost3 = Ghost(2,8, maze, behaviour)
                return [ghost1, ghost2, ghost3]

            elif maze_size == MazeSize.LARGE:
                ghost1 = Ghost(5,4, maze, behaviour)
                ghost2 = Ghost(22,2, maze, behaviour)
                ghost3 = Ghost(4,14, maze, behaviour)
                ghost4 = Ghost(8,9, maze, behaviour)
                ghost5 = Ghost(16,5, maze, behaviour)
                ghost6 = Ghost(15,3, maze, behaviour)
                ghost7 = Ghost(18,14, maze, behaviour)
                return [ghost1, ghost2, ghost3, ghost4, ghost5, ghost6, ghost7]
            
        if search_algorithm_enum == SearchAlgoType.MINIMAX:
            if maze_size == MazeSize.SMALL:
                ghost1 = MinimaxGhost(4,5, maze, GhostBehaviour.INTELLIGENT)
                ghost2 = MinimaxGhost(7,1, maze, GhostBehaviour.INTELLIGENT)
                ghost3 = MinimaxGhost(10,4, maze, GhostBehaviour.INTELLIGENT)
                return [ghost1, ghost2, ghost3]

            elif maze_size == MazeSize.MEDIUM:
                ghost1 = MinimaxGhost(10,6, maze, GhostBehaviour.INTELLIGENT)
                ghost2 = MinimaxGhost(4,14, maze, GhostBehaviour.INTELLIGENT)
                ghost3 = MinimaxGhost(2,8, maze, GhostBehaviour.INTELLIGENT)
                return [ghost1, ghost2, ghost3]

            elif maze_size == MazeSize.LARGE:
                ghost1 = MinimaxGhost(5,4, maze, GhostBehaviour.INTELLIGENT)
                ghost2 = MinimaxGhost(22,2, maze, GhostBehaviour.INTELLIGENT)
                ghost3 = MinimaxGhost(4,14, maze, GhostBehaviour.INTELLIGENT)
                return [ghost1, ghost2, ghost3]
        return []