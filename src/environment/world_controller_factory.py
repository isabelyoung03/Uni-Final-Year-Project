from src.agents.Player import Player
from src.agents.ghost_list_factory import GhostListFactory
from src.agents.player_factory import PlayerFactory
from src.enums.search_algorithm_type import SearchAlgoType
from src.environment.Goal import Goal
from src.environment.Goal_factory import GoalFactory
from src.environment.a_star_world_controller import AStarWorldController
from src.environment.world_controller import WorldController
from src.search_algorithms.algorithm_factory import SearchAlgorithmFactory

"""
Factory class for creating a new WorldController
"""
class WorldControllerFactory:
    """
    Creates and returns a new WorldController
    """
    @staticmethod
    def create_new(maze, search_algorithm_enum) -> WorldController:
        goals = GoalFactory.get_goals(maze, search_algorithm_enum)
        search_algorithm = SearchAlgorithmFactory.create_new(search_algorithm_enum, maze, goals)
        player = PlayerFactory.get_player(maze, search_algorithm)
        if search_algorithm_enum == SearchAlgoType.A_STAR or search_algorithm_enum == SearchAlgoType.A_STAR_VS_GREEDY:
            return AStarWorldController(maze, player, goals)
        ghosts = GhostListFactory.get_ghost_list(maze, search_algorithm_enum)
        return WorldController(maze, player, ghosts, goals[0])