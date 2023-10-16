from agents.Ghost import Ghost
from agents.Player import Player
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
        ghosts = [Ghost(5,4)]
        return WorldController(maze, player, ghosts)