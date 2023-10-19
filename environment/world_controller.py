import sys
import pygame
from gui.button import Button
import config
from gui.icon_buttton import IconButton

class WorldController:
    def __init__(self, maze, player, ghosts, goal):
        self.maze = maze
        self.player = player
        self.ghosts = ghosts
        self.goal = goal
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))
        self.timer = pygame.time.Clock()
        self.movement_delay = 300 
        maze_width = maze.get_maze_size().get_width() - 200 #200 is the space left over for buttons
        self.home_button = IconButton("Home.png", maze_width + 15, 15, 32, 32, True)
        self.play_button = IconButton("Play.png", maze_width + 50, 18, 32, 32, False)
        self.pause_button = IconButton("Pause.png", maze_width + 55, 15, 32, 34, True)

    def player_decide(self):
        return self.player.decide()

    """
    Update the player
    """
    def update_player(self, action):
        self.player.execute(action)

    """
    Get the player to calculate its path to the goal as the environment has changed
    """
    def player_calculate_path(self):
        opponent_locations = []
        for ghost in self.ghosts:
            opponent_locations.append(ghost.get_location())
        self.player.find_path(opponent_locations)

    def ghosts_decide(self):
        ghost_actions = []
        for ghost in self.ghosts:
            ghost_actions.append(ghost.decide())
        return ghost_actions

    """
    Update each the ghosts

    Return true if any of the ghosts have changed position, otherwise false
    """
    def update_ghosts(self, ghost_actions):
        changes = False
        for i in range(len(ghost_actions)):
            if self.ghosts[i].execute(ghost_actions[i]):
                changes = True
        return changes

    """
    Render world on the screen
    """
    def render(self):
        self.screen.fill(config.BLACK)
        self.maze.display_maze(self.screen)
        self.goal.draw(self.screen)
        self.player.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        self.home_button.draw(self.screen)
        self.play_button.draw(self.screen)
        self.pause_button.draw(self.screen)
        pygame.display.flip()

    """
    Runs the maze on the screen
    """
    def run(self):
        pygame.display.set_caption(self.maze.maze_size.to_string() + " maze using " + self.player.search_algo_string() + " search")
        self.render()
        self.player_calculate_path()
        MOVE_AGENTS = pygame.USEREVENT + 1 #event for moving player when it is time
        pygame.time.set_timer(MOVE_AGENTS, self.movement_delay)
        cycle_count = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_button.handle_event(event):
                        return True #go back to menu page
                    elif self.pause_button.handle_event(event) and not self.goal.get_achieved():
                        self.pause_button.toggle(True)
                        self.play_button.toggle(False)
                    elif self.play_button.handle_event(event) and not self.goal.get_achieved():
                        self.pause_button.toggle(False)
                        self.play_button.toggle(True)
                    elif self.play_button.handle_event(event):
                        self.pause_button.toggle(False)
                        self.play_button.toggle(True)
                elif event.type == MOVE_AGENTS and not self.goal.get_achieved() and not self.pause_button.get_toggled():
                    print("--- Cycle " + str(cycle_count) + " ---")
                    self.cycle()
                    cycle_count += 1
                self.render()

    def cycle(self):
        player_action = self.player_decide() #decide players next move
        ghost_actions = self.ghosts_decide() #decide all ghosts next moves
        self.update_player(player_action)
        if self.update_ghosts(ghost_actions): #if any ghosts move when they execute their next move
            self.player_calculate_path() #recalculate player path for next round
        if self.player.get_location() == self.goal.get_location(): #if player reached goal
            self.goal.set_achieved()
            self.play_button.toggle(True)
            self.pause_button.toggle(True)
            print("Reached goal!")
        self.render()