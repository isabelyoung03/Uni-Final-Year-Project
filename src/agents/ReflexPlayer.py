import pygame
from src.search_algorithms.manhattan_distance import ManhattanDistance
from src.agents.Player import Player
from src.enums.action import Action

"""
Reflex Player class that models the player as a reflex agent. Inherits from Player.
"""
class ReflexPlayer(Player):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, None)
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
    Check is the move is possible and away from a ghost
    """
    def check_safe_move(self, x, y) -> bool:
        if not self.check_valid_move(x, y):
            return False
        if ( #if new location has an opponent in the surrounding squares that could move 
            self.ghost_in_location(x + 1, y)
            or self.ghost_in_location(x - 1, y)
            or self.ghost_in_location(x, y + 1)
            or self.ghost_in_location(x, y - 1)
        ):
            return False
        return True #true if valid move with no opponent in cell and an uneaten cupcake
    
    """
    Check if the move is sensible: it is possible and there is a cupcake in the square
    """
    def check_sensible_move(self, x, y) -> bool:
        if not self.uneaten_cupcake_in_location(x,y):
            return False
        return self.check_safe_move(x,y)

    """
    Get all of the possible moves from the current location
    """  
    def get_possible_moves(self) -> list:
        possible_moves = []
        if self.check_sensible_move(self.x + 1, self.y):
            possible_moves.append(Action.RIGHT)
        if self.check_sensible_move(self.x - 1, self.y):
            possible_moves.append(Action.LEFT)
        if self.check_sensible_move(self.x, self.y + 1):
            possible_moves.append(Action.DOWN)
        if self.check_sensible_move(self.x, self.y - 1):
            possible_moves.append(Action.UP)
        return possible_moves
    
    """
    Get possible moves to avoid nearby ghost
    """
    def evade_ghost_moves(self) -> list:
        possible_moves = []
        if self.check_safe_move(self.x + 1, self.y):
            possible_moves.append(Action.RIGHT)
        if self.check_safe_move(self.x - 1, self.y):
            possible_moves.append(Action.LEFT)
        if self.check_safe_move(self.x, self.y + 1):
            possible_moves.append(Action.DOWN)
        if self.check_safe_move(self.x, self.y - 1):
            possible_moves.append(Action.UP)
        return possible_moves
    
    """
    Backtrack to previous location
    """
    def backtrack(self) -> Action:
        if self.move_memory:
            previous_location = self.move_memory[-1] #peek
            if self.check_safe_move(previous_location[0], previous_location[1]):
                self.move_memory.pop()
                return self.move_towards(previous_location[0], previous_location[1])
            else:
                return self.move_away_from_ghost()
        else:
            if not self.check_safe_move(self.x, self.y): #if move isn't safe aka there is a ghost close
                return self.move_away_from_ghost()
            return Action.IDLE
        
    """
    Choose a move to move away from a nearby ghost
    """
    def move_away_from_ghost(self) -> Action:
        print("moving away from ghost")
        possible_moves = self.evade_ghost_moves()
        if possible_moves == []:
            return Action.IDLE
        self.move_memory.append((self.x, self.y))
        return possible_moves[0]

    """
    Move towards a location based on the current location
    """
    def move_towards(self, goal_x, goal_y) -> Action:
        x_dif = goal_x - self.x
        y_dif = goal_y - self.y
        if abs(x_dif) == 1 and y_dif == 0:
            if x_dif > 0:
                return Action.RIGHT  
            else: return Action.LEFT
        elif x_dif == 0 and abs(y_dif) == 1:
            if y_dif > 0:
                return Action.DOWN
            else: return Action.UP
        else:
            return Action.IDLE
        
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
        print(self.move_memory)
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