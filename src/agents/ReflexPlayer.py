import pygame
from src.search_algorithms.manhattan_distance import ManhattanDistance
from src.agents.Player import Player
from src.enums.action import Action

"""
Reflex Player class that models the player as a reflex agent. Inherits from Player.
"""
class ReflexPlayer(Player):
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

    """
    Check if there is a ghost in the location specified
    """
    def ghost_in_location(self,x,y) -> bool:
        for ghost in self.ghosts:
            if ghost.get_location() == (x,y):
                return True
        return False

    """
    Check if there is an uneaten cupcake in the location specified
    """
    def uneaten_cupcake_in_location(self, x, y) -> bool:
        for cupcake in self.cupcakes:
            if cupcake.get_location() == (x,y) and not cupcake.get_achieved():
                return True
        return False

    """
    Check is a move to the given location is valid (aka not a wall or a ghost)
    Avoiding a square with a ghost in gives the agent the property of rationality
    """
    def check_valid_move(self, x, y) -> bool:
        if not self.maze.check_valid_location(x,y):
            return False
        if self.ghost_in_location(x,y):
             return False
        return True
    
    """
    Check is the move is possible and reasonable
    """
    def check_possible_move(self, x, y) -> bool:
        if not self.check_valid_move(x, y):
            return False
        if not self.uneaten_cupcake_in_location(x,y):
            return False
        return True #true if valid move with no opponent in cell and an uneaten cupcake

    """
    Get all of the possible moves from the current location
    """  
    def get_possible_moves(self) -> list:
        possible_moves = []
        if self.check_possible_move(self.x + 1, self.y):
            possible_moves.append(Action.RIGHT)
        if self.check_possible_move(self.x - 1, self.y):
            possible_moves.append(Action.LEFT)
        if self.check_possible_move(self.x, self.y + 1):
            possible_moves.append(Action.DOWN)
        if self.check_possible_move(self.x, self.y - 1):
            possible_moves.append(Action.UP)
        return possible_moves
    
    """
    Backtrack to previous location
    """
    def backtrack(self) -> Action:
        if not self.move_memory:
            return Action.IDLE
        previous_location = self.move_memory.pop()
        return self.move_towards(previous_location[0], previous_location[1])

    """
    Move towards a location based on the current location
    """
    def move_towards(self, goal_x, goal_y) -> Action:
        x_dif = goal_x - self.x
        y_dif = goal_y - self.y
        if abs(x_dif) >= abs(y_dif):
            if x_dif > 0:
                return Action.RIGHT 
            else:
                return Action.LEFT
        else:
            if y_dif > 0:
                return Action.DOWN
            else:
                return Action.UP
        
    """
    Decide which action to take
    """
    def decide(self) -> Action:
        possible_moves = self.get_possible_moves()
        if possible_moves == []:
            self.backtracking = True
            return self.backtrack()
        self.backtracking = False
        return possible_moves[0]

    """
    Execute a given action
    """
    def execute(self, action) -> None:
        if not self.backtracking:
            self.move_memory.append((self.x, self.y))
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
