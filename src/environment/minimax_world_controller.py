import sys
import pygame
from src.environment.WorldState import WorldState
from src.search_algorithms.minimax import Minimax
from src.environment.world_controller import WorldController
import config
from src.gui.icon_buttton import IconButton
from src.gui.menu import display_text

"""
Special world controller for modelling the Minimax and Expecimax algorithms
"""
class MinimaxWorldController(WorldController):
    def __init__(self, maze, player, ghosts, cupcakes):
        self.maze = maze
        self.player = player
        self.player.set_goal_location(cupcakes[0].get_location())
        ghosts[0].set_goal_location(self.player.get_location())
        self.ghosts = [ghosts[0]]
        self.goals = [cupcakes[0]]
        self.cupcakes = self.goals
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))
        self.timer = pygame.time.Clock()
        self.movement_delay = 300
        self.maze_width = maze.get_maze_size().get_width() - 200
        self.home_button = IconButton("Home.png", self.maze_width + 15, 15, 32, 32, True)
        self.play_button = IconButton("Play.png", self.maze_width + 50, 18, 32, 32, True)
        self.pause_button = IconButton("Pause.png", self.maze_width + 55, 15, 32, 34, False)
        self.cycle_count = 0
        self.game_lost = False
        self.minimax = Minimax(maze, self.goals[0])

    """
    Render world on the screen
    """
    def render(self) -> None:
        self.screen.fill(config.BLACK)
        self.maze.display_maze(self.screen)
        self.ghosts[0].draw(self.screen)
        self.cupcakes[0].draw(self.screen)
        if not self.game_lost:
            self.player.draw(self.screen)
        self.home_button.draw(self.screen)
        self.play_button.draw(self.screen)
        self.pause_button.draw(self.screen)

        if self.goals[0].get_achieved():
            display_text('Goal achieved!', 20, config.WHITE, self.maze_width + 95, 300, self.screen)
            display_text('In ' + str(self.cycle_count) + ' moves', 15, config.WHITE, self.maze_width + 95, 320, self.screen)
        elif self.game_lost:
            display_text('Player loses!', 20, config.WHITE, self.maze_width + 95, 100, self.screen)
        pygame.display.flip()

    """
    Runs the maze on the screen
    """
    def run(self) -> None:
        pygame.display.set_caption(self.maze.maze_size.to_string() + " maze for Minimax agents")
        MOVE_AGENTS = pygame.USEREVENT + 1 #event for moving player when it is time
        pygame.time.set_timer(MOVE_AGENTS, self.movement_delay)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                elif event.type == MOVE_AGENTS and not self.goals[0].get_achieved() and not self.pause_button.get_toggled() and not self.game_lost:
                    print("--- Cycle " + str(self.cycle_count) + " ---")
                    self.cycle()
                    self.cycle_count += 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_button.handle_event(event):
                        return #go back to menu page
                    elif self.pause_button.handle_event(event) and not self.goals[0].get_achieved():
                        self.pause_button.toggle(True)
                        self.play_button.toggle(False)
                    elif self.play_button.handle_event(event) and not self.goals[0].get_achieved():
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
        world_state = WorldState(self.maze, self.ghosts, self.goals, self.player.get_location())
        self.player.revise(world_state)
        self.ghosts[0].revise(world_state)
        player_action = self.minimax.get_best_move(self.player, self.ghosts[0], True) #decide method for player
        ghost_action = self.minimax.get_best_move(self.player, self.ghosts[0], False) #decide method for ghost
        self.player.execute(player_action) 
        self.ghosts[0].execute(ghost_action)
        self.update_goals()
        if self.all_goals_achieved():
            self.play_button.toggle(True)
            self.pause_button.toggle(True)
            print("Reached goal!")
        if super().player_caught():
            self.game_lost = True
            print("Player has been caught!")
        self.render()