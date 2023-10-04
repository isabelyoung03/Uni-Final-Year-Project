import pygame
from agents.Agent import Agent
import config 

class Player(Agent):
    """
    The player class for the program.
    Has starting coordinates and can be moved a square in any direction.
    Different sprite images based on direction travelling.
    
    startX: starting position x coord
    startY: starting position y coord

    """

    def __init__(self, x, y, maze_map):
        Agent.__init__(self, x, y, maze_map)

        self.sprite_width = 7
        self.sprite_height = 12

        transformation = (self.sprite_width*config.pixel_scale, self.sprite_height*config.pixel_scale)

        self.down_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Down.png"), transformation)

        self.up_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Up.png"), transformation)

        self.right_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Right.png"), transformation)

        self.left_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Left.png"), transformation)

        self.current_sprite = self.down_sprite
    
    """
    Moves player to the square to the left
    """
    def move_left(self):
        self.current_sprite = self.left_sprite
        nextNode = self.map[self.y][self.x-1]
        if nextNode == ' ' or nextNode == 'G':
            self.x = self.x - 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square to the right
    """
    def move_right(self):
        self.current_sprite = self.right_sprite
        nextNode = self.map[self.y][self.x+1]
        if nextNode == ' ' or nextNode == 'G':
            self.x = self.x + 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square below
    """
    def move_down(self):
        self.current_sprite = self.down_sprite
        nextNode = self.map[self.y+1][self.x]
        if nextNode == ' ' or nextNode == 'G':
            self.y = self.y + 1
        print("Player at " + str(self.get_location()))

    """
    Moves player to the square above
    """
    def move_up(self):
        self.current_sprite = self.up_sprite
        nextNode = self.map[self.y-1][self.x]
        if nextNode == ' ' or nextNode == 'G':
            self.y = self.y - 1
        print("Player at " + str(self.get_location()))
    
    """
    Draws the player on the screen
    """
    def draw(self, screen):
        screen_x_coord = self.x*config.square_size + self.sprite_height
        screen_y_coord = self.y*config.square_size + self.sprite_width
        screen.blit(self.current_sprite, dest = (screen_x_coord, screen_y_coord))
