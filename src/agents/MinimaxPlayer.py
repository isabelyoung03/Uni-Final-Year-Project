from src.agents.MinimaxAgent import MinimaxAgent
from src.search_algorithms.manhattan_distance import ManhattanDistance
from src.agents.Player import Player
from src.enums.action import Action

"""
Player that uses minimax to find the best move. Inherits from MinimaxAgent.
"""
class MinimaxPlayer(MinimaxAgent):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.maze = None
        self.ghosts = None
        self.cupcake = None
        self.move_memory = []
        self.backtracking = False

    def move_left(self) -> None:
        super().move_left()

    def move_right(self) -> None:
        super().move_right()

    def move_down(self) -> None:
        super().move_down()

    def move_up(self) -> None:
        super().move_up()
