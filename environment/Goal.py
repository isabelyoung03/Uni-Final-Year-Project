import pygame
import config

class Goal():
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.achieved = False
        transformation = (32, 32)
        self.cupcake_sprite = pygame.transform.scale(pygame.image.load("gui/resources/Cupcake.png"), transformation)

    """
    Draws the goal on the screen if goal not achieved
    """
    def draw(self, screen):
        if not self.achieved:
            screen_x_coord = self.x * config.SQUARE_SIZE  + 8
            screen_y_coord = self.y * config.SQUARE_SIZE + 8
            screen.blit(self.cupcake_sprite, dest=(screen_x_coord, screen_y_coord))

    """
    Sets the goal to achieved
    """
    def set_achieved(self):
        self.achieved = True

    """
    Return true if goal achieved, otherwise false
    """
    def get_achieved(self):
        return self.achieved
    
    """
    Returns location of goal
    """
    def get_location(self):
        return (self.x, self.y)