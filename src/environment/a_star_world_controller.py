import sys
import pygame
from src.enums.search_algorithm_type import SearchAlgoType
from src.environment.world_controller import WorldController
from src.gui.button_group import ButtonGroup
from src.gui.button import Button
import config
from src.gui.icon_buttton import IconButton
from src.gui.menu import display_text
from src.gui.option_button import OptionButton
from src.search_algorithms.euclidian_distance import EuclidianDistance
from src.search_algorithms.manhattan_distance import ManhattanDistance

"""
Special world controller for the A star only world. Has option to choose heuristic used.
"""
class AStarWorldController(WorldController):
    def __init__(self, maze, player, goals):
        self.maze = maze
        self.player = player
        self.goals = goals #start with one goal for now
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))
        self.timer = pygame.time.Clock()
        self.movement_delay = config.SPEED
        self.maze_width = maze.get_maze_size().get_width() - 200 #200 is the space left over for buttons
        self.home_button = IconButton("Home.png", self.maze_width + 15, 15, 32, 32, True)
        self.play_button = IconButton("Play.png", self.maze_width + 50, 18, 32, 32, True)
        self.pause_button = IconButton("Pause.png", self.maze_width + 55, 15, 32, 34, False)
        manhattan = OptionButton('Manhattan Distance', 16, config.GREEN, config.BLACK, self.maze_width + 20, 130, ManhattanDistance)
        euclidian = OptionButton('Euclidean Distance', 16, config.GREEN, config.BLACK, self.maze_width + 22, 155, EuclidianDistance)
        self.heuristic_button_group = ButtonGroup([manhattan, euclidian])
        self.cycle_count = 0
        self.heuristic = None

    """
    Get players decision for next action
    """
    def player_decide(self):
        return self.player.decide()

    """
    Update the player
    """
    def update_player(self, action) -> None:
        self.player.execute(action)

    """
    Find out of all the goals in the maze have been reached
    """
    def all_goals_achieved(self) -> bool:
        for goal in self.goals:
            if not goal.get_achieved():
                return False
        return True

    """
    Update goal if player is at the same location
    """
    def update_goals(self) -> None:
        for goal in self.goals:
            if self.player.get_location() == goal.get_location(): #if player at goal location
                goal.set_achieved()
    """
    Render world on the screen
    """
    def render(self) -> None:
        self.screen.fill(config.BLACK)
        self.maze.display_maze(self.screen)
        for goal in self.goals:
            goal.draw(self.screen)
        self.player.draw(self.screen)
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
    def run(self) -> None:
        pygame.display.set_caption(self.maze.maze_size.to_string() + " maze using " + self.player.search_algo_string() + " search")
        self.update_goals()
        self.render()
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
                elif event.type == MOVE_AGENTS and not self.all_goals_achieved() and not self.pause_button.get_toggled():
                    print("--- Cycle " + str(self.cycle_count) + " ---")
                    self.cycle()
                    self.cycle_count += 1
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
                self.render()

    """
    Complete one cycle, updating everyone in the maze
    """
    def cycle(self) -> None:
        self.player_calculate_path() #update path at each step as next goal may already have been achieved when going to another goal
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
    def get_heuristic(self) -> bool:
        while self.heuristic == None:
            for event in pygame.event.get():
                self.heuristic_button_group.handle_event(event)
                if event.type == pygame.QUIT:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_button.handle_event(event):
                        return True #go back to menu page
                    elif self.play_button.handle_event(event): #if play button is pressed
                        self.heuristic = self.heuristic_button_group.get_result()
                        self.player.get_search_algorithm().set_heuristic(self.heuristic) #change A* heuristic
                        self.pause_button.toggle(False)
                        self.play_button.toggle(True)
                        self.player_calculate_path()
                self.render()
        return False

    """
    Get the player to calculate its path to the goal as the environment has changed
    """
    def player_calculate_path(self) -> None:
        self.player.find_path()