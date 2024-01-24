import pygame
from src.agents.Agent import Agent
import config
from src.enums.action import Action
from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm 

class Player(Agent):
    """
    The player class for the program.
    Has starting coordinates and can be moved a square in any direction.
    Different sprite images based on direction travelling.
    
    x: starting position x coord
    y: starting position y coord

    """

    def __init__(self, x:int, y:int, search_algorithm:SearchAlgorithm = None):
        Agent.__init__(self, x, y)
        self.x = x
        self.y = y
        self.search_algorithm = search_algorithm
        transformation = (config.SPRITE_WIDTH*config.PIXEL_SCALE, config.SPRITE_HEIGHT*config.PIXEL_SCALE)

        self.down_sprite = pygame.transform.scale(pygame.image.load("src/gui/resources/Down.png"), transformation)
        self.up_sprite = pygame.transform.scale(pygame.image.load("src/gui/resources/Up.png"), transformation)
        self.right_sprite = pygame.transform.scale(pygame.image.load("src/gui/resources/Right.png"), transformation)
        self.left_sprite = pygame.transform.scale(pygame.image.load("src/gui/resources/Left.png"), transformation)

        self.current_sprite = self.down_sprite
        
        self.path_index = 0

        self.path_to_follow = None
    
    """
    Moves player to the square to the left
    """
    def move_left(self) -> None:
        self.current_sprite = self.left_sprite
        self.x = self.x - 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square to the right
    """
    def move_right(self) -> None:
        self.current_sprite = self.right_sprite
        self.x = self.x + 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square below
    """
    def move_down(self) -> None:
        self.current_sprite = self.down_sprite
        self.y = self.y + 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square above
    """
    def move_up(self) -> None:
        self.current_sprite = self.up_sprite
        self.y = self.y - 1
        print("Player at " + str(self.get_location()))
    
    """
    Draws the player on the screen
    """
    def draw(self, screen) -> None:
        screen_x_coord = self.x*config.SQUARE_SIZE + config.SPRITE_HEIGHT
        screen_y_coord = self.y*config.SQUARE_SIZE + config.SPRITE_WIDTH
        screen.blit(self.current_sprite, dest = (screen_x_coord, screen_y_coord))

    """
    Decide on a path to follow based on the search algorithm
    """
    def find_path(self, opponent_locations=None) -> None:
        if opponent_locations is None:
            path = self.search_algorithm.search(self.x, self.y)
        else:
            path = self.search_algorithm.search(self.x, self.y, opponent_locations)

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

    """
    Decide on a next move and return action
    """
    def decide(self) -> Action:
        return self.follow_path()

    """
    Returns players search algorithm as a string
    """
    def search_algo_string(self) -> str:
        return self.search_algorithm.get_enum().value
    
    """
    Returns players search algorithm
    """
    def get_search_algorithm(self) -> SearchAlgorithm:
        return self.search_algorithm