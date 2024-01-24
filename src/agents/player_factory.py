"""
Factory class for creating player
"""
from src.agents.MinimaxPlayer import MinimaxPlayer
from src.agents.ReflexPlayer import ReflexPlayer
from src.agents.Player import Player
from src.enums.search_algorithm_type import SearchAlgoType
from src.enums.size import MazeSize

"""
Gets the player based on the maze size and algorithm type
"""
class PlayerFactory:
    """
    Returns player object for a given maze
    """
    @staticmethod
    def get_player(maze, search_algorithm) -> Player:
        maze_size = maze.get_maze_size()
        player_x = 1
        player_y = 1
        if search_algorithm.get_enum() == SearchAlgoType.A_STAR or search_algorithm.get_enum() == SearchAlgoType.GREEDY or search_algorithm.get_enum() == SearchAlgoType.REFLEX:
            if maze_size == MazeSize.SMALL:
                player_x = 6
                player_y = 4

            elif maze_size == MazeSize.MEDIUM:
                player_x = 8
                player_y = 8

            elif maze_size == MazeSize.LARGE:
                player_x = 12
                player_y = 7
        
        if search_algorithm.get_enum() == SearchAlgoType.REFLEX:
            return ReflexPlayer(player_x, player_y)
        
        if search_algorithm.get_enum() == SearchAlgoType.MINIMAX:
            return MinimaxPlayer(player_x, player_y)
        
        return Player(player_x, player_y, search_algorithm)