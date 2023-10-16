from agents.Player import Player
from agents.ghost_list_factory import GhostListFactory
from environment.world_controller import WorldController
from search_algorithms.algorithm_factory import SearchAlgorithmFactory

"""
Factory class for creating a new WorldController
"""
class WorldControllerFactory:
    @staticmethod
    def create_new(maze, player_x, player_y, search_algorithm_enum):
        search_algorithm = SearchAlgorithmFactory.create_new(search_algorithm_enum, maze)
        player = Player(player_x, player_y, search_algorithm)
        ghosts = GhostListFactory.get_ghost_list(maze, search_algorithm_enum)
        return WorldController(maze, player, ghosts)