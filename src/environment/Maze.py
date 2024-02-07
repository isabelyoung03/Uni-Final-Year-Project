import pygame
import config

class Maze:
    """ A maze which will be displayed on the screen
        Initiated with a map of the maze, map can be overrided
    """
    def __init__(self, maze_size, the_map=None):
        if not the_map:
            self.map = maze_size.value
        else:
            self.map = the_map #override  map
        self.maze_size = maze_size

        squareScale = (48,48)
        self.leaves = pygame.image.load("src/gui/resources/Leaves.png")
        self.leaves = pygame.transform.scale(self.leaves, squareScale)

        self.path = pygame.image.load("src/gui/resources/Path.png")
        self.path = pygame.transform.scale(self.path, squareScale)

        self.cupcake = pygame.image.load("src/gui/resources/Cupcake.png")
        self.cupcake = pygame.transform.scale(self.cupcake, (32,32))
    
    """ 
    Displays the maze on the screen based on the map for the maze
    """
    def display_maze(self, screen) -> None:
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

    #checks if the location is not a barrier
    def check_valid_location(self, x, y) -> bool:
        location = self.map[y][x]
        return location != 'X' and location != '|' and location != '-' and location != '+'

    #Return maze size enum
    def get_maze_size(self) -> int:
        return self.maze_size
    
    #Return map as a 2D array
    def get_map(self) -> list:
        return self.map
