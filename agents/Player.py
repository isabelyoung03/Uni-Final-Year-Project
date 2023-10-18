import time
import pygame
from agents.Agent import Agent
import config
from enums.search_algorithm_type import SearchAlgoType 

class Player(Agent):
    """
    The player class for the program.
    Has starting coordinates and can be moved a square in any direction.
    Different sprite images based on direction travelling.
    
    x: starting position x coord
    y: starting position y coord

    """

    def __init__(self, x, y, search_algorithm):
        Agent.__init__(self, x, y, search_algorithm)
        self.x = x
        self.y = y
        self.goal_achieved = False

        transformation = (config.SPRITE_WIDTH*config.PIXEL_SCALE, config.SPRITE_HEIGHT*config.PIXEL_SCALE)

        self.down_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Down.png"), transformation)
        self.up_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Up.png"), transformation)
        self.right_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Right.png"), transformation)
        self.left_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Left.png"), transformation)

        self.current_sprite = self.down_sprite

        self.strict_path = None #strict path to follow for depth-first and breadth-first as no opponents
        self.path_index = 0

        print(search_algorithm.get_enum())
        if search_algorithm.get_enum() == SearchAlgoType.BREADTH or search_algorithm.get_enum() == SearchAlgoType.DEPTH:
            self.strict_path = self.find_path()
    
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
    def find_path(self):
        path = self.search_algorithm.search(self.x, self.y)
        if path:
            print(path)
            print("Path found to goal! Following...")
            return path
        else:
            print("No solution to goal!")
        return []

    """
    Follow the path from the algorithm - for depth and breadth first
    """
    def follow_path(self):
        if self.path_index < len(self.strict_path):
            i, j = self.strict_path[self.path_index]
            if i - self.x == 1:
                self.move_right()
            elif i - self.x == -1:
                self.move_left()
            elif j - self.y == 1:
                self.move_down()
            elif j - self.y == -1:
                self.move_up()
            self.path_index += 1 

    """
    Decide on a next move
    """
    def decide(self):
        if self.strict_path is not None:
            self.follow_path()
        else:
            print("Making decisions...")