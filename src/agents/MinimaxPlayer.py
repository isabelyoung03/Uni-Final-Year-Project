from src.environment.WorldState import WorldState
from src.environment.Goal import Goal
from src.search_algorithms.a_star import AStarSearch
from src.agents.Player import Player
from src.search_algorithms.minimax_state import State

"""
Player that uses minimax to find the best move. Inherits from MinimaxAgent.
"""
class MinimaxPlayer(Player):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.maze = None
        self.goal_location = None

    """
    Update internal representation for the maze map, locations of the ghosts and cupcakes not yet eaten
    """
    def revise(self, world_state: WorldState) -> None:
       super().revise(world_state)

    """
    Set goal location
    """
    def set_goal_location(self, goal_location):
        self.goal_location = goal_location
