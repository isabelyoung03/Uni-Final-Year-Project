import pygame
from src.agents.Player import Player
from src.agents.Agent import Agent
import config
from src.enums.action import Action
from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm 

"""
Reflex Player class that models the player as a reflex agent. Inherits from Player.
"""
class ReflexPlayer(Player):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, None)
        self.maze = None
        self.ghosts = None
        self.cupcake = None

    def move_left(self) -> None:
        super().move_left()

    def move_right(self) -> None:
        super().move_right()

    def move_down(self) -> None:
        super().move_down()

    def move_up(self) -> None:
        super().move_up()

    def decide(self) -> Action:
        return Action.DOWN

    def execute(self, action) -> None:
        if action == Action.DOWN:
            self.move_down()
        elif action == Action.LEFT:
            self.move_left()
        elif action == Action.RIGHT:
            self.move_right()
        elif action == Action.UP:
            self.move_up()

    """
    Update internal representation for the maze map, locations of the ghosts and cupcakes not yet eaten
    """
    def revise(self, maze, ghosts, cupcakes) -> None:
        self.maze = maze
        self.ghosts = ghosts
        self.cupcakes = cupcakes
