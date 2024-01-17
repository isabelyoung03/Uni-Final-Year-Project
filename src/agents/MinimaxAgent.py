from src.enums.action import Action
from src.agents.Agent import Agent

"""
Minimax agent class for agents that use the minimax algorithm to calculate the best move
"""
class MinimaxAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    """
    Evaluates a position in the maze and returns a score.
    Score is calculated based on distance to goal and closeness to walls and opponents.
    """
    def evaluate(x,y):
        pass

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