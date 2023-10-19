from agents.Player import Player
from agents.ghost_list_factory import GhostListFactory
from environment.Goal import Goal
from environment.Goal_factory import GoalFactory
from environment.world_controller import WorldController
from search_algorithms.algorithm_factory import SearchAlgorithmFactory

"""
Factory class for creating a new WorldController
"""
class WorldControllerFactory:
    @staticmethod
    def create_new(maze, player_x, player_y, search_algorithm_enum):
        goal = GoalFactory.get_goal(maze)
        search_algorithm = SearchAlgorithmFactory.create_new(search_algorithm_enum, maze, goal)
        player = Player(player_x, player_y, search_algorithm, goal)
        ghosts = GhostListFactory.get_ghost_list(maze, search_algorithm_enum)
        return WorldController(maze, player, ghosts, goal)