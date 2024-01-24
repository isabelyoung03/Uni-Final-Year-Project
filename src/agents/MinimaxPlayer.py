from src.agents.Player import Player
from src.search_algorithms.minimax_state import State

"""
Player that uses minimax to find the best move. Inherits from MinimaxAgent.
"""
class MinimaxPlayer(Player):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.maze = None
        
    """
    Evaluates a position in the maze and returns a score.
    Score is calculated based on distance to goal and closeness to walls and opponents.
    """
    def evaluate(self, state: State):
        (x, y) = state.get_player_location()
        wall_penalty = -5
        opponent_penalty = -10
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        eval_score = 30

        for dx, dy in directions:
            if not self.maze.check_valid_location(x + dx, y + dy): #if cell is a wall
                eval_score += wall_penalty
            elif (x + dx, y + dy) == state.get_ghost_location(): #if opponent in cell
                eval_score += opponent_penalty

        return eval_score
