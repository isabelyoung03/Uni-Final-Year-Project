import pygame

class Maze:
    """ A maze which will be displayed on the screen
        Initiated with a map of the maze
    """
    def __init__(self, map):
        self.map = map
        squareScale = (48,48)
        self.square_size = 50
        self.leaves = pygame.image.load("resources/Leaves.png")
        self.leaves = pygame.transform.scale(self.leaves, squareScale)

        self.path = pygame.image.load("resources/Path.png")
        self.path = pygame.transform.scale(self.path, squareScale)

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
                        pygame.draw.rect(screen, (255,165,0), pygame.Rect(x, y, self.square_size, self.square_size))
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
                x += self.square_size
            y += self.square_size