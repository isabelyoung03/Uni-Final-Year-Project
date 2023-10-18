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

    """
    Update the player
    """
    def update_player(self):
        self.player.decide()

    """
    Get the player to calculate its path to the goal as the environment has changed
    """
    def player_calculate_path(self):
        opponent_locations = []
        for ghost in self.ghosts:
            opponent_locations.append(ghost.get_location())
        self.player.find_path(opponent_locations)

    """
    Update each the ghosts

    Return true if any of the ghosts have changed position, otherwise false
    """
    def update_ghosts(self):
        changes = False
        for ghost in self.ghosts:
            if ghost.decide():
                changes = True
        return changes

    """
    Render world on the screen
    """
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
        self.player_calculate_path()
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
                    if self.update_ghosts(): #if any ghosts move
                        self.player_calculate_path() #recalculate player path
                    self.update_player()
                    self.render()
