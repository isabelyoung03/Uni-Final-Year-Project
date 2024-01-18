import random
import pygame
from src.environment import Goal
from src.agents.Agent import Agent
import config
from src.enums.action import Action
from src.enums.ghost_behaviour import GhostBehaviour 

class Ghost(Agent):
    """
    The Ghost class for the program
    
    x: starting position x coord
    y: starting position y coord
    behaviour: behaviour enum of the ghost

    """

    def __init__(self, x, y, maze, behaviour):
        Agent.__init__(self, x, y)

        transformation = (8*config.PIXEL_SCALE, 12*config.PIXEL_SCALE)

        self.right_sprite = pygame.transform.scale(pygame.image.load("src/gui/resources/Ghost_Right.png"), transformation)
        self.left_sprite = pygame.transform.scale(pygame.image.load("src/gui/resources/Ghost_Left.png"), transformation)

        self.current_sprite = self.left_sprite

        self.map = maze.get_map()
        self.behaviour = behaviour

        self.goal = None
    
    """
    Moves ghost to the square to the left

    Returns true if move successful, otherwise false
    """
    def move_left(self) -> bool:
        nextNode = self.map[self.y][self.x-1]
        if nextNode == ' ':
            self.x = self.x - 1
            self.current_sprite = self.left_sprite
            return True
        return False

    """
    Moves ghost to the square to the right

    Returns true if move successful, otherwise false
    """
    def move_right(self) -> bool:
        nextNode = self.map[self.y][self.x+1]
        if nextNode == ' ':
            self.x = self.x + 1
            self.current_sprite = self.right_sprite
            return True
        return False

    """
    Moves ghost to the square below

    Returns true if move successful, otherwise false
    """
    def move_down(self) -> bool:
        nextNode = self.map[self.y+1][self.x]
        if nextNode == ' ':
            self.y = self.y + 1
            return True
        return False

    """
    Moves ghost to the square above

    Returns true if move successful, otherwise false
    """
    def move_up(self) -> bool:
        nextNode = self.map[self.y-1][self.x]
        if nextNode == ' ':
            self.y = self.y - 1
            return True
        return False
    
    """
    Draws the ghost on the screen
    """
    def draw(self, screen) -> None:
        screen_x_coord = self.x*config.SQUARE_SIZE + config.SPRITE_HEIGHT
        screen_y_coord = self.y*config.SQUARE_SIZE + config.SPRITE_WIDTH
        screen.blit(self.current_sprite, dest = (screen_x_coord, screen_y_coord))

    """
    Decide on a path to follow based on the search algorithm
    """
    def find_path(self, player_location) -> None:
        print(player_location)
        path = self.search_algorithm.search(self.x, self.y)
        if path:
            self.path_to_follow = path
            self.path_index = 0
        else:
            print("No solution to goal!")

    """
    Follow the path from the algorithm - for depth and breadth first
    """
    def follow_path(self) -> Action:
        action = Action.IDLE
        if self.path_to_follow is not None:
            if self.path_index < len(self.path_to_follow):
                i, j = self.path_to_follow[self.path_index]
                if ((i,j) == (self.x, self.y)): #if already at next location in path to be followed
                    self.path_index += 1 
                    i, j = self.path_to_follow[self.path_index] #get the next location
                if i - self.x == 1:
                    action = Action.RIGHT
                elif i - self.x == -1:
                    action = Action.LEFT
                elif j - self.y == 1:
                    action = Action.DOWN
                elif j - self.y == -1:
                    action = Action.UP
                self.path_index += 1 
        return action
    
    def check_player_nearby(self) -> Action:
        if self.player_location == (self.x + 1, self.y):
            return Action.RIGHT
        if self.player_location == (self.x - 1, self.y):
            return Action.LEFT
        if self.player_location == (self.x, self.y + 1):
            return Action.DOWN
        if self.player_location == (self.x, self.y - 1):
            return Action.UP
        return None

    """
    Decide on a next move

    Returns Action enum
    """
    def decide(self) -> Action:
        if self.behaviour == GhostBehaviour.RANDOM or self.behaviour == GhostBehaviour.RANDOM_CHASE:
            action = self.check_player_nearby()
            if action and self.behaviour == GhostBehaviour.RANDOM_CHASE:
                print("Chasing player!")
                return action
            
            random_integer = random.randint(1,4)
            if random_integer == 1:
                return Action.DOWN
            elif random_integer == 2:
                return Action.LEFT
            elif random_integer == 3:
                return Action.RIGHT
            elif random_integer == 4:
                return Action.UP
        return Action.IDLE
    
    """
    Execute specified action
    """
    def execute(self, action) -> bool:
        if action == Action.DOWN:
            self.move_down()
        elif action == Action.LEFT:
            self.move_left()
        elif action == Action.RIGHT:
            self.move_right()
        elif action == Action.UP:
            self.move_up()
        else:
            return False #did not move
        return True