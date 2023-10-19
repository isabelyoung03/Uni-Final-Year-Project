import time
import pygame
from agents.Agent import Agent
import config
from enums.action import Action
from enums.search_algorithm_type import SearchAlgoType 

class Player(Agent):
    """
    The player class for the program.
    Has starting coordinates and can be moved a square in any direction.
    Different sprite images based on direction travelling.
    
    x: starting position x coord
    y: starting position y coord

    """

    def __init__(self, x, y, search_algorithm, goal):
        Agent.__init__(self, x, y, search_algorithm)
        self.x = x
        self.y = y
        self.goal = goal

        transformation = (config.SPRITE_WIDTH*config.PIXEL_SCALE, config.SPRITE_HEIGHT*config.PIXEL_SCALE)

        self.down_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Down.png"), transformation)
        self.up_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Up.png"), transformation)
        self.right_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Right.png"), transformation)
        self.left_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Left.png"), transformation)

        self.current_sprite = self.down_sprite

        self.strict_path = None #strict path to follow for depth-first and breadth-first as no opponents
        self.path_index = 0

        self.path_to_follow = None
    
    """
    Moves player to the square to the left
    """
    def move_left(self):
        self.current_sprite = self.left_sprite
        self.x = self.x - 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square to the right
    """
    def move_right(self):
        self.current_sprite = self.right_sprite
        self.x = self.x + 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square below
    """
    def move_down(self):
        self.current_sprite = self.down_sprite
        self.y = self.y + 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square above
    """
    def move_up(self):
        self.current_sprite = self.up_sprite
        self.y = self.y - 1
        print("Player at " + str(self.get_location()))
    
    """
    Draws the player on the screen
    """
    def draw(self, screen):
        screen_x_coord = self.x*config.SQUARE_SIZE + config.SPRITE_HEIGHT
        screen_y_coord = self.y*config.SQUARE_SIZE + config.SPRITE_WIDTH
        screen.blit(self.current_sprite, dest = (screen_x_coord, screen_y_coord))

    """
    Decide on a path to follow based on the search algorithm (only for breadth or depth first search)
    """
    def find_path(self, opponent_locations):
        path = self.search_algorithm.search(self.x, self.y, opponent_locations)
        if path:
            print("Updated path to goal! Following...")
            self.path_to_follow = path
            self.path_index = 0
        else:
            print("No solution to goal!")

    """
    Follow the path from the algorithm - for depth and breadth first
    """
    def follow_path(self):
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
        if action == Action.IDLE:
            print("Path to follow: " + str(self.path_to_follow))
        return action

    """
    Decide on a next move
    """
    def decide(self):
        return self.follow_path()

    """
    Execute specified action
    """
    def execute(self, action):
        if action == Action.DOWN:
            self.move_down()
        elif action == Action.LEFT:
            self.move.left()
        elif action == Action.RIGHT:
            self.move_right()
        elif action == Action.UP:
            self.move_up()

    """
    Returns players search algorithm as a string
    """
    def search_algo_string(self):
        return self.search_algorithm.get_enum().value