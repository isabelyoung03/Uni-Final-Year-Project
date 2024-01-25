from src.environment.WorldState import WorldState
from src.environment.Goal import Goal
from src.search_algorithms.a_star import AStarSearch
from src.agents.Ghost import Ghost
from src.search_algorithms.minimax_state import State

"""
Ghosts that uses minimax to find the best move. Inherits from MinimaxAgent.
"""
class MinimaxGhost(Ghost):
    def __init__(self, x: int, y: int, maze, behaviour):
        super().__init__(x, y, maze, behaviour)
        self.maze = None
        self.a_star_search = None
        
    """
    Evaluates a position in the maze and returns a score.
    Score is calculated based on distance to goal and closeness to walls and opponents.
    """
    def evaluate(self, state: State) -> int:
        (x, y) = state.get_ghost_location()
        eval_score = 0
        player_bonus = 100 #bonus for reaching the player

        distance_to_goal = len(self.a_star_search.search(x,y))
        eval_score += player_bonus / (distance_to_goal + 1)
        return eval_score
    
    """
    Update internal representation for the maze map, locations of the ghosts and cupcakes not yet eaten
    """
    def revise(self, world_state: WorldState) -> None:
       super().revise(world_state)
       self.a_star_search = AStarSearch(self.maze,  [Goal(self.goal_location[0], self.goal_location[1])])

    """
    Set goal location
    """
    def set_goal_location(self, goal_location):
        self.goal_location = goal_location