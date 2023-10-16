import pygame
from agents.Agent import Agent
import config 

class Ghost(Agent):
    """
    The Ghost class for the program
    
    x: starting position x coord
    y: starting position y coord

    """

    def __init__(self, x, y):
        Agent.__init__(self, x, y, None)

        transformation = (8*config.PIXEL_SCALE, 12*config.PIXEL_SCALE)

        self.right_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Ghost_Right.png"), transformation)
        self.left_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Ghost_Left.png"), transformation)

        self.current_sprite = self.left_sprite
    
    """
    Moves ghost to the square to the left
    """
    def move_left(self):
        self.current_sprite = self.left_sprite
        self.x = self.x - 1
        print("Ghost at " + str(self.get_location()))

    """
    Moves ghost to the square to the right
    """
    def move_right(self):
        self.current_sprite = self.right_sprite
        self.x = self.x + 1
        print("Ghost at " + str(self.get_location()))

    """
    Moves ghost to the square below
    """
    def move_down(self):
        self.y = self.y + 1
        print("Ghost at " + str(self.get_location()))

    """
    Moves ghost to the square above
    """
    def move_up(self):
        self.y = self.y - 1
        print("Ghost at " + str(self.get_location()))
    
    """
    Draws the ghost on the screen
    """
    def draw(self, screen):
        screen_x_coord = self.x*config.SQUARE_SIZE + config.SPRITE_HEIGHT
        screen_y_coord = self.y*config.SQUARE_SIZE + config.SPRITE_WIDTH
        screen.blit(self.current_sprite, dest = (screen_x_coord, screen_y_coord))