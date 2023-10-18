import random
import pygame
from agents.Agent import Agent
import config
from enums.ghost_behaviour import GhostBehaviour 

class Ghost(Agent):
    """
    The Ghost class for the program
    
    x: starting position x coord
    y: starting position y coord
    behaviour: behaviour enum of the ghost

    """

    def __init__(self, x, y, maze, behaviour):
        Agent.__init__(self, x, y, None)

        transformation = (8*config.PIXEL_SCALE, 12*config.PIXEL_SCALE)

        self.right_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Ghost_Right.png"), transformation)
        self.left_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Ghost_Left.png"), transformation)

        self.current_sprite = self.left_sprite

        self.map = maze.get_map()
        self.behaviour = behaviour
    
    """
    Moves ghost to the square to the left
    """
    def move_left(self):
        nextNode = self.map[self.y][self.x-1]
        if nextNode == ' ':
            self.x = self.x - 1
            self.current_sprite = self.left_sprite

    """
    Moves ghost to the square to the right
    """
    def move_right(self):
        nextNode = self.map[self.y][self.x+1]
        if nextNode == ' ':
            self.x = self.x + 1
            self.current_sprite = self.right_sprite

    """
    Moves ghost to the square below
    """
    def move_down(self):
        nextNode = self.map[self.y+1][self.x]
        if nextNode == ' ':
            self.y = self.y + 1

    """
    Moves ghost to the square above
    """
    def move_up(self):
        nextNode = self.map[self.y-1][self.x]
        if nextNode == ' ':
            self.y = self.y - 1
    
    """
    Draws the ghost on the screen
    """
    def draw(self, screen):
        screen_x_coord = self.x*config.SQUARE_SIZE + config.SPRITE_HEIGHT
        screen_y_coord = self.y*config.SQUARE_SIZE + config.SPRITE_WIDTH
        screen.blit(self.current_sprite, dest = (screen_x_coord, screen_y_coord))

    """
    Decide on a next move
    """
    def decide(self):
        if self.behaviour == GhostBehaviour.RANDOM:
            random_integer = random.randint(1, 5)
            if random_integer == 1:
                self.move_down()
            elif random_integer == 2:
                self.move_left()
            elif random_integer == 3:
                self.move_right()
            elif random_integer == 4:
                self.move_up()

        elif self.behaviour == GhostBehaviour.INTELLIGENT:
            pass #add intelligence here...