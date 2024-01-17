from src.enums.action import Action
from src.agents.Agent import Agent

"""
Minimax agent class for agents that use the minimax algorithm to calculate the best move
"""
class MinimaxAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.maze = None
    
    """
    Evaluates a position in the maze and returns a score.
    Score is calculated based on distance to goal and closeness to walls and opponents.
    """
    def evaluate(self, x, y):
        wall_penalty = -5
        opponent_penalty = -10
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        eval_score = 30

        for dx, dy in directions:
            if not self.maze.check_valid_location(x + dx, y + dy): #if cell is a wall
                eval_score += wall_penalty
            elif self.check_valid_move(x + dx, y + dy): #if opponent in cell
                eval_score += opponent_penalty

    """
    Minimax function to get the best action for the agent
    """
    def minimax(self) -> Action:
        pass

    """
    Decide function of the agent
    """
    def decide(self) -> Action:
        return self.minimax()
    
