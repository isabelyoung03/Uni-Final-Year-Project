import sys
import pygame
from environment.world_controller import WorldController
from gui.button_group import ButtonGroup
from gui.button import Button
import config
from gui.icon_buttton import IconButton
from gui.menu import display_text
from gui.option_button import OptionButton
from search_algorithms.manhattan_distance import ManhattanDistance

"""
Special world controller for the A star only world. Has option to choose heuristic used.
"""
class AStarWorldController(WorldController):
    def __init__(self, maze, player, goals):
        self.maze = maze
        self.player = player
        self.goals = goals
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))
        self.timer = pygame.time.Clock()
        self.movement_delay = config.SPEED 
        self.maze_width = maze.get_maze_size().get_width() - 200 #200 is the space left over for buttons
        self.home_button = IconButton("Home.png", self.maze_width + 15, 15, 32, 32, True)
        self.play_button = IconButton("Play.png", self.maze_width + 50, 18, 32, 32, True)
        self.pause_button = IconButton("Pause.png", self.maze_width + 55, 15, 32, 34, False)
        manhattan = OptionButton('Manhattan Distance', 16, config.GREEN, config.BLACK, self.maze_width + 20, 130, ManhattanDistance)
        heuristic2 = OptionButton('Heuristic Two', 16, config.GREEN, config.BLACK, self.maze_width + 40, 155, ManhattanDistance)
        self.heuristic_button_group = ButtonGroup([manhattan, heuristic2])
        self.cycle_count = 0

    """
    Find out of all the goals in the maze have been reached
    """
    def all_goals_achieved(self):
        for goal in self.goals:
            if not goal.get_achieved():
                return False
        return True

    """
    Update goal if player is at the same location
    """
    def update_goals(self):
        for goal in self.goals:
            if self.player.get_location() == goal.get_location(): #if player at goal location
                self.goal.set_achieved()
    """
    Render world on the screen
    """
    def render(self):
        self.screen.fill(config.BLACK)
        self.maze.display_maze(self.screen)
        self.goals[0].draw(self.screen)
        self.player.draw(self.screen)
        for goal in self.goals:
            goal.draw(self.screen)
        self.home_button.draw(self.screen)
        self.play_button.draw(self.screen)
        self.pause_button.draw(self.screen)
        display_text('A* Heuristic:', 18, config.WHITE, self.maze_width + 90, 100, self.screen)
        self.heuristic_button_group.draw(self.screen)

        if self.all_goals_achieved():
            display_text('Goal achieved!', 20, config.WHITE, self.maze_width + 95, 300, self.screen)
            display_text('In ' + str(self.cycle_count) + ' moves', 15, config.WHITE, self.maze_width + 95, 320, self.screen)

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
        while True:
            if self.get_heuristic():
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_button.handle_event(event):
                        return #go back to menu page
                    elif self.pause_button.handle_event(event) and not self.all_goals_achieved():
                        self.pause_button.toggle(True)
                        self.play_button.toggle(False)
                    elif self.play_button.handle_event(event) and not self.all_goals_achieved():
                        self.pause_button.toggle(False)
                        self.play_button.toggle(True)
                    elif self.play_button.handle_event(event):
                        self.pause_button.toggle(False)
                        self.play_button.toggle(True)
                elif event.type == MOVE_AGENTS and not self.all_goals_achieved() and not self.pause_button.get_toggled():
                    print("--- Cycle " + str(self.cycle_count) + " ---")
                    self.cycle()
                    self.cycle_count += 1
                self.render()

    """
    Complete one cycle, updating everyone in the maze
    """
    def cycle(self):
        player_action = self.player_decide() #decide players next move
        self.update_player(player_action)
        self.update_goals()
        if self.all_goals_achieved():
            self.play_button.toggle(True)
            self.pause_button.toggle(True)
            print("Reached goal!")
        self.render()

    """
    Get the heuristic from the button group until play button is pressed
    """
    def get_heuristic(self):
        heuristic = None
        while heuristic == None:
            for event in pygame.event.get():
                self.heuristic_button_group.handle_event(event)
                if event.type == pygame.QUIT:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_button.handle_event(event):
                        return True #go back to menu page
                    elif self.play_button.handle_event(event): #if play button is pressed
                        heuristic = self.heuristic_button_group.get_result()
                        self.player.get_search_algorithm().set_heuristic(heuristic) #change A* heuristic
                        self.pause_button.toggle(False)
                        self.play_button.toggle(True)
                self.render()

    """
    Get the player to calculate its path to the goal as the environment has changed
    """
    def player_calculate_path(self):
        self.player.find_path()