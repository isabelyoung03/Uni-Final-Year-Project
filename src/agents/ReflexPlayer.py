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

    def get_possible_moves(self) -> list:
        possible_moves = []
        print("Possible moves:")
        if self.maze.check_valid_location(self.x + 1, self.y):
            print("RIGHT")
            possible_moves.append(Action.RIGHT)
        if self.maze.check_valid_location(self.x - 1, self.y):
            print("LEFT")
            possible_moves.append(Action.LEFT)
        if self.maze.check_valid_location(self.x, self.y + 1):
            print("DOWN")
            possible_moves.append(Action.DOWN)
        if self.maze.check_valid_location(self.x, self.y - 1):
            print("UP")
            possible_moves.append(Action.UP)
        return possible_moves

    def decide(self) -> Action:
        self.get_possible_moves()
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
