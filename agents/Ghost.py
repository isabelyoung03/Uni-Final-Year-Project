import random
import pygame
from agents.Agent import Agent
import config
from enums.action import Action
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

    Returns true if move successful, otherwise false
    """
    def move_left(self):
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
    def move_right(self):
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
    def move_down(self):
        nextNode = self.map[self.y+1][self.x]
        if nextNode == ' ':
            self.y = self.y + 1
            return True
        return False

    """
    Moves ghost to the square above

    Returns true if move successful, otherwise false
    """
    def move_up(self):
        nextNode = self.map[self.y-1][self.x]
        if nextNode == ' ':
            self.y = self.y - 1
            return True
        return False
    
    """
    Draws the ghost on the screen
    """
    def draw(self, screen):
        screen_x_coord = self.x*config.SQUARE_SIZE + config.SPRITE_HEIGHT
        screen_y_coord = self.y*config.SQUARE_SIZE + config.SPRITE_WIDTH
        screen.blit(self.current_sprite, dest = (screen_x_coord, screen_y_coord))

    """
    Decide on a next move

    Returns tAction enum
    """
    def decide(self):
        if self.behaviour == GhostBehaviour.RANDOM:
            random_integer = random.randint(1, 5)
            if random_integer == 1:
                return Action.DOWN
            elif random_integer == 2:
                return Action.LEFT
            elif random_integer == 3:
                return Action.RIGHT
            elif random_integer == 4:
                return Action.UP
        elif self.behaviour == GhostBehaviour.INTELLIGENT:
            pass #add intelligence here...
        return Action.IDLE
    
    """
    Execute specified action
    """
    def execute(self, action):
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