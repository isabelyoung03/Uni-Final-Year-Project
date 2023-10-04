import sys

import pygame
from environment.Maze import Maze
from agents.Player import Player
import config

class MazeSearch:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        
        pygame.display.set_caption("Menu")

        self.player = Player(1,1, config.small_maze)
        self.smallMaze = Maze(config.small_maze)

    def check_events(self):
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