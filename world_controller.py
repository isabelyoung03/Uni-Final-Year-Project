import sys
import pygame
import config

class WorldController:
    def __init__(self, maze, player):
        self.maze = maze
        self.player = player
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))

    def update_player(self):
        self.player.decide()

    def render(self):
        self.screen.fill(config.BLACK)
        self.maze.display_maze(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    """
    Runs the maze on the screen
    """
    def run(self):
        pygame.display.set_caption(self.maze.maze_size.to_string() + " Maze")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_UP:
                    #     self.player.move_up()
                    # elif event.key == pygame.K_DOWN:
                    #     self.player.move_down()
                    # elif event.key == pygame.K_RIGHT:
                    #     self.player.move_right()
                    # elif event.key == pygame.K_LEFT:
                    #     self.player.move_left()
                    if event.key == pygame.K_q:
                        sys.exit()
            self.player.decide()
            self.render()