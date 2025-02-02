from src.environment.human_world_controller import HumanWorldController
from src.environment.expectimax_world_controller import ExpectimaxWorldController
from src.environment.minimax_world_controller import MinimaxWorldController
from src.environment.reflex_agent_world_controller import ReflexAgentWorldController
from src.agents.ghost_list_factory import GhostListFactory
from src.agents.player_factory import PlayerFactory
from src.enums.search_algorithm_type import SearchAlgoType
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
    def create_new(maze, search_algorithm_enum, no_of_opponents=None) -> WorldController:
        goals = GoalFactory.get_goals(maze, search_algorithm_enum)
        search_algorithm = SearchAlgorithmFactory.create_new(search_algorithm_enum, maze, goals)
        player = PlayerFactory.get_player(maze, search_algorithm)

        if search_algorithm_enum == SearchAlgoType.A_STAR or search_algorithm_enum == SearchAlgoType.A_STAR_ALL_CELLS or search_algorithm_enum == SearchAlgoType.GREEDY:
            return AStarWorldController(maze, player, goals)
        
        ghosts = GhostListFactory.get_ghost_list(maze, search_algorithm_enum)
        if search_algorithm_enum == SearchAlgoType.REFLEX:
            player = PlayerFactory.get_player(maze, search_algorithm)
            return ReflexAgentWorldController(maze, player, ghosts, goals)
        
        if search_algorithm_enum == SearchAlgoType.MINIMAX:
            player = PlayerFactory.get_player(maze, search_algorithm)
            return MinimaxWorldController(maze, player, ghosts[:no_of_opponents], goals)
        
        if search_algorithm_enum == SearchAlgoType.EXPECTIMAX:
            player = PlayerFactory.get_player(maze, search_algorithm)
            return ExpectimaxWorldController(maze, player, ghosts[:no_of_opponents], goals)
        
        if search_algorithm_enum == SearchAlgoType.HUMAN:
            player = PlayerFactory.get_player(maze, search_algorithm)
            return HumanWorldController(maze, player, ghosts, goals)
        
        return WorldController(maze, player, ghosts, goals[0])