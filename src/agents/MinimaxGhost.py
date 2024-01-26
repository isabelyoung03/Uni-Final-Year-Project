from src.environment.WorldState import WorldState
from src.agents.Ghost import Ghost

"""
Ghosts that uses minimax to find the best move. Inherits from MinimaxAgent.
"""
class MinimaxGhost(Ghost):
    def __init__(self, x: int, y: int, maze, behaviour):
        super().__init__(x, y, maze, behaviour)
        self.maze = None
        
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