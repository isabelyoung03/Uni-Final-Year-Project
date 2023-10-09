import sys
import pygame
import config

class Maze:
    """ A maze which will be displayed on the screen
        Initiated with a map of the maze
    """
    def __init__(self, maze_size, player):
        self.map = maze_size.value
        self.maze_size = maze_size
        self.player = player

        squareScale = (48,48)
        self.leaves = pygame.image.load("gui/resources/Leaves.png")
        self.leaves = pygame.transform.scale(self.leaves, squareScale)

        self.path = pygame.image.load("gui/resources/Path.png")
        self.path = pygame.transform.scale(self.path, squareScale)

        self.cupcake = pygame.image.load("gui/resources/Cupcake.png")
        self.cupcake = pygame.transform.scale(self.cupcake, (32,32))

        self.maze_screen = pygame.display.set_mode((maze_size.get_width(), maze_size.get_height()))
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


    """
    Runs the small maze on the screen
    """
    def run(self):
        pygame.display.set_caption(self.maze_size.to_string() + " Maze")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.player.move_down()
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    elif event.key == pygame.K_LEFT:
                        self.player.move_left()
                    elif event.key == pygame.K_q:
                        sys.exit()
            self.update_maze_screen()
        
    """
    Updates the maze screen as changes happen
    """
    def update_maze_screen(self):
        self.maze_screen.fill(config.BLACK)
        self.display_maze(self.maze_screen)
        self.player.draw(self.maze_screen)
        pygame.display.flip()