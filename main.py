import sys

import pygame
from Maze import Maze
from Player import Player
import mazes

class MazeSearch:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        
        pygame.display.set_caption("Menu")

        self.smallMaze = Maze(mazes.small_maze)
        self.player = Player(50, 50)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        pygame.display.flip()
        self.smallMaze.display_maze(self.screen)
        self.player.draw(self.screen)

if __name__ == '__main__':
    maze_search = MazeSearch()
    maze_search.run_game()