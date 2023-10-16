import sys
import pygame
import config

class WorldController:
    def __init__(self, maze, player, ghosts):
        self.maze = maze
        self.player = player
        self.ghosts = ghosts
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))
        self.timer = pygame.time.Clock()
        self.movement_delay = 500 

    def update_player(self):
        self.player.decide()

    def update_ghosts(self):
        for ghost in self.ghosts:
            ghost.move_right()

    def render(self):
        self.screen.fill(config.BLACK)
        self.maze.display_maze(self.screen)
        self.player.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        pygame.display.flip()

    """
    Runs the maze on the screen
    """
    def run(self):
        pygame.display.set_caption(self.maze.maze_size.to_string() + " Maze")
        MOVE_AGENTS = pygame.USEREVENT + 1 #event for moving player when it is time
        pygame.time.set_timer(MOVE_AGENTS, self.movement_delay)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                elif event.type == MOVE_AGENTS:
                        self.update_ghosts()
                        self.update_player()
                        self.render()
