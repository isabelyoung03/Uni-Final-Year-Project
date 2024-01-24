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
        opponent_penalty = -40
        eval_score = 0

        surrounding_cells = self.get_surrounding_cells(x, y)
        ghost_location = state.get_ghost_location()

        for (i, j) in surrounding_cells:
            if not self.maze.check_valid_location(i, j):  #if cell is a wall
                eval_score += wall_penalty
            elif (i, j) == ghost_location:  #if ghost in cell
                eval_score += opponent_penalty

            ghosts_surrounding_cells = self.get_surrounding_cells(ghost_location[0], ghost_location[1])
            for cell in ghosts_surrounding_cells:
                if cell == (i,j):
                    eval_score += opponent_penalty/2  # smaller score decrease if player nearby

        return eval_score
