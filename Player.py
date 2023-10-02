import pygame
class Player:
    """
    The player class for the program.
    Has starting coordinates and can be moved a square in any direction.
    Different sprite images based on direction travelling.
    """

    def __init__(self, startX, startY):
        self.x = startX+12
        self.y = startY+8
        self.speed = 1
        self.scale = 3

        self.sprite_width = 7
        self.sprite_height = 12

        self.down_sprite = pygame.transform.scale(pygame.image.load("resources/Down.png"), (self.sprite_width*self.scale, self.sprite_height*self.scale))

        self.up_sprite = pygame.transform.scale(pygame.image.load("resources/Up.png"), (self.sprite_width*self.scale, self.sprite_height*self.scale))

        self.right_sprite = pygame.transform.scale(pygame.image.load("resources/Right.png"), (self.sprite_width*self.scale, self.sprite_height*self.scale))

        self.left_sprite = pygame.transform.scale(pygame.image.load("resources/Left.png"), (self.sprite_width*self.scale, self.sprite_height*self.scale))

        self.current_sprite = self.down_sprite

    """
    Moves player to the square above
    """
    def moveUp(self, ticks):
        self.y = self.y - self.speed
        self.current_sprite = self.up_sprite

    """
    Moves player to the square below
    """
    def moveDown(self, ticks):
        self.y = self.y + self.speed
        self.current_sprite = self.down_sprite

    """
    Moves player to the square to the right
    """
    def moveRight(self, ticks):
        self.x = self.x + self.speed
        self.current_sprite = self.right_sprite

    """
    Moves player to the square to the left
    """
    def moveLeft(self, ticks):
        self.x = self.x - self.speed
        self.current_sprite = self.left_sprite
    
    """
    Draws the player on the screen
    """
    def draw(self, screen):
        screen.blit(self.current_sprite, dest = (self.x, self.y))
