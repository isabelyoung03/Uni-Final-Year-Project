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

        eval_score = 30

        surrounding_cells = self.get_surrounding_cells(x, y)
        player_location = state.get_player_location()

        for (i, j) in surrounding_cells:
            if not self.maze.check_valid_location(i, j):  #if cell is a wall
                eval_score += wall_penalty
            elif (i, j) == player_location:  #if player in cell
                eval_score += 100

            players_surrounding_cells = self.get_surrounding_cells(player_location[0], player_location[1])
            for cell in players_surrounding_cells:
                if cell == (i,j):
                    eval_score += 30  # maller score increase if player nearby

        return eval_score