import pygame
import config

class Maze:
    """ A maze which will be displayed on the screen
        Initiated with a map of the maze
    """
    def __init__(self, map):
        self.map = map
        squareScale = (48,48)
        self.leaves = pygame.image.load("gui/resources/Leaves.png")
        self.leaves = pygame.transform.scale(self.leaves, squareScale)

        self.path = pygame.image.load("gui/resources/Path.png")
        self.path = pygame.transform.scale(self.path, squareScale)

        self.cupcake = pygame.image.load("gui/resources/Cupcake.png")
        self.cupcake = pygame.transform.scale(self.cupcake, (32,32))

    def display_maze(self, screen):
        """ Displays the maze on the screen based on the map for the maze
        """
        y = 0
        for i in self.map:
            x = 0
            char_array = [char for char in i]
            for c in char_array:
                match c:
                    case 'G':
                        screen.blit(self.path, dest = (x,y))
                        screen.blit(self.cupcake, dest = (x+8,y+8))
                    case 'X':
                        screen.blit(self.leaves, dest = (x,y))
                    case '|':
                        screen.blit(self.leaves, dest = (x,y))
                    case '-':
                        screen.blit(self.leaves, dest = (x,y))
                    case '+':
                        screen.blit(self.leaves, dest = (x,y))
                    case _:
                        screen.blit(self.path, dest = (x,y))
                x += config.SQUARE_SIZE
            y += config.SQUARE_SIZE