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
        self.a_star_search = None
        
    """
    Evaluates a position in the maze and returns a score.
    Score is calculated based on distance to goal and closeness to walls and opponents.
    """
    def evaluate(self, state: State):
        (x, y) = state.get_player_location()
        wall_penalty = -10
        opponent_penalty = -50
        eval_score = 0
        goal_bonus = 100

        distance_to_goal = len(self.a_star_search.search(x,y))
        eval_score += goal_bonus / (distance_to_goal + 1)

        surrounding_cells = self.get_surrounding_cells(x, y)
        ghost_location = state.get_ghost_location()

        for (i, j) in surrounding_cells:
            if not self.maze.check_valid_location(i, j):
                eval_score += wall_penalty

            if (i, j) == ghost_location:
                eval_score += opponent_penalty

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
