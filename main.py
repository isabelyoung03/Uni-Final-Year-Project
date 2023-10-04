import sys

import pygame
from agents.Player import Player
from environment.Maze import Maze
import config

class MazeSearch:
    def __init__(self):
        pygame.init()
        self.maze = None
        self.menu_screen = pygame.display.set_mode((config.MENU_SCREEN_WIDTH, config.MENU_SCREEN_HEIGHT))
        self.maze_screen = None
        self.player = None

    """
    Displays the maze selection menu and returns the selected maze
    """
    def maze_selection_menu(self):
        pygame.display.set_caption("Menu")
        selected_maze = None
        while selected_maze == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        selected_maze = config.small_maze
            self.menu_screen.fill((0, 0, 0))
            pygame.display.flip()
        return selected_maze

    """
    Runs the small maze on the screen
    """
    def run_small_maze(self):
        pygame.display.set_caption("Small Maze")
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
            self.update_maze_screen(self.maze_screen)

    
    """
    Updates the maze screen as changes happen
    """
    def update_maze_screen(self, screen):
        pygame.display.flip()
        self.maze.display_maze(screen)
        self.pl
        
    """
    Runs the program
    """
    def run(self):
        while True:
            selected_maze = self.maze_selection_menu()
            pygame.display.set_caption("Small Maze")
            self.maze_screen = pygame.display.set_mode((config.SMALL_MAZE_SCREEN_WIDTH, config.SMALL_MAZE_SCREEN_HEIGHT))
            self.player = Player(1, 1, selected_maze)
            self.maze = Maze(selected_maze)
            self.run_small_maze()

if __name__ == '__main__':
    maze_search = MazeSearch()
    maze_search.run()