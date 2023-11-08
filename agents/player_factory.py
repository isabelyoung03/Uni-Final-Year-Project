"""
Factory class for creating player
"""
from agents.Ghost import Ghost
from agents.Player import Player
from enums.ghost_behaviour import GhostBehaviour
from enums.search_algorithm_type import SearchAlgoType
from enums.size import MazeSize

"""
Gets the player based on the maze size and algorithm type
"""
class PlayerFactory:
    @staticmethod
    def get_player(maze, search_algorithm) -> Player:
        maze_size = maze.get_maze_size()
        player_x = 1
        player_y = 1
        if maze_size == MazeSize.SMALL and search_algorithm.get_enum() == SearchAlgoType.A_STAR:
            player_x = 6
            player_y = 4

        elif maze_size == MazeSize.MEDIUM and search_algorithm.get_enum() == SearchAlgoType.A_STAR:
            player_x = 8
            player_y = 8

        elif maze_size == MazeSize.LARGE and search_algorithm.get_enum() == SearchAlgoType.A_STAR:
            player_x = 12
            player_y = 7

        return Player(player_x, player_y, search_algorithm)