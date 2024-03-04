from src.agents.Player import Player
from src.enums.action import Action

"""
Player controlled by the human
"""
class HumanPlayer(Player):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    def valid_move(self, action:Action):
        x = self.x
        y = self.y
        if action == Action.RIGHT:
            x += 1
        elif action == Action.LEFT:
            x -= 1
        elif action == Action.UP:
            y -= 1
        elif action == Action.DOWN:
            y += 1
        if self.maze.check_valid_location(x,y):
            return True
        else:
            return False
    

