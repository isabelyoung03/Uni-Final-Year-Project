import sys
import pygame
import config

class WorldController:
    def __init__(self, maze, player):
        self.maze = maze
        self.player = player
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))
        self.timer = pygame.time.Clock()
        self.movement_delay = 500 

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
                    if event.key == pygame.K_q:
                        sys.exit()
            self.follow_path(self.player.decide())
            self.render()
        
    """
    Follow the path from the algorithm
    """
    def follow_path(self, path):
        MOVE_PLAYER = pygame.USEREVENT + 1 #event for moving player when it is time
        pygame.time.set_timer(MOVE_PLAYER, self.movement_delay)
        path_index = 0  

        while path_index < len(path):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == MOVE_PLAYER:
                    if path_index < len(path):
                        i, j = path[path_index]
                        if j - self.player.x == 1:
                            self.player.move_right()
                        if j - self.player.x == -1:
                            self.player.move_left()
                        if i - self.player.y == 1:
                            self.player.move_down()
                        if i - self.player.y == -1:
                            self.player.move_up()
                        path_index += 1 
            self.render()  