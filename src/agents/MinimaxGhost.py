from src.agents.Ghost import Ghost
from src.search_algorithms.minimax_state import State

"""
Ghosts that uses minimax to find the best move. Inherits from MinimaxAgent.
"""
class MinimaxGhost(Ghost):
    def __init__(self, x: int, y: int, maze, behaviour):
        super().__init__(x, y, maze, behaviour)
        self.maze = None
        
    """
    Evaluates a position in the maze and returns a score.
    Score is calculated based on distance to goal and closeness to walls and opponents.
    """
    def evaluate(self, state: State):
        (x, y) = state.get_ghost_location()
        wall_penalty = -5
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        eval_score = 30

        for dx, dy in directions:
            if not self.maze.check_valid_location(x + dx, y + dy): #if cell is a wall
                eval_score += wall_penalty
            elif (x + dx, y + dy) == state.get_player_location(): #if player in cell
                eval_score += 100

        return eval_score