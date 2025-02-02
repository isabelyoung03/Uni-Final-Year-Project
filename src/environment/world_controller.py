import sys
import pygame
from src.analysis.analyse import Analysis
import config
from src.enums import search_algorithm_type
from src.environment.WorldState import WorldState
from src.enums.action import Action
from src.gui.button import Button
from src.gui.icon_buttton import IconButton
from src.gui.menu import display_text

"""
Runs the maze on the screen for a world with one single goal
"""
class WorldController:
    def __init__(self, maze, player, ghosts, goal):
        self.maze = maze
        self.player = player
        self.ghosts = ghosts
        self.goal = goal
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))
        self.timer = pygame.time.Clock()
        self.movement_delay = config.SPEED 
        self.maze_width = maze.get_maze_size().get_width() - 200 #200 is the space left over for buttons
        self.home_button = IconButton("Home.png", self.maze_width + 15, 15, 32, 32, True)
        self.play_button = IconButton("Play.png", self.maze_width + 50, 18, 32, 32, True)
        self.pause_button = IconButton("Pause.png", self.maze_width + 55, 15, 32, 34, False)
        self.search_algorithm_enum = player.get_search_algorithm().get_enum()
        if self.search_algorithm_enum != search_algorithm_type.SearchAlgoType.UNIFORM:
            self.analysis_button = Button('Analyse', 12, config.BLACK, config.WHITE, self.maze_width + 40, 300, 100, 30)
        self.cycle_count = 0
        self.game_lost = False
        self.analysed = False

    """
    Get players decision for next action
    """
    def player_decide(self) -> Action:
        return self.player.decide()

    """
    Update the player
    """
    def update_player(self, action: Action):
        self.player.execute(action)

    """
    Get the player to calculate its path to the goal as the environment has changed
    """
    def player_calculate_path(self) -> None:
        opponent_locations = []
        for ghost in self.ghosts:
            opponent_locations.append(ghost.get_location())
        self.player.find_path(opponent_locations)

    """
    Make each ghost decide on its next action
    """
    def ghosts_decide(self) -> list:
        ghost_actions = []
        for ghost in self.ghosts:
            ghost_actions.append(ghost.decide())
        return ghost_actions

    """
    Update each the ghosts

    Return true if any of the ghosts have changed position, otherwise false
    """
    def update_ghosts(self, ghost_actions) -> bool:
        changes = False
        for i in range(len(ghost_actions)):
            if self.ghosts[i].execute(ghost_actions[i]):
                changes = True
        return changes

    """
    Render world on the screen
    """
    def render(self) -> None:
        self.screen.fill(config.BLACK)
        self.maze.display_maze(self.screen)
        self.goal.draw(self.screen)
        if not self.game_lost:
            self.player.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        self.home_button.draw(self.screen)
        self.play_button.draw(self.screen)
        self.pause_button.draw(self.screen)
        if self.search_algorithm_enum != search_algorithm_type.SearchAlgoType.UNIFORM:
            self.analysis_button.draw(self.screen)
            if self.analysed:
                display_text('Results in /results folder', 14, config.WHITE, self.maze_width + 100, 350, self.screen)
        if self.goal.get_achieved():
            display_text('Goal achieved!', 20, config.WHITE, self.maze_width + 95, 100, self.screen)
            display_text('In ' + str(self.cycle_count) + ' moves', 15, config.WHITE, self.maze_width + 95, 120, self.screen)
        elif self.game_lost:
            display_text('Player loses!', 20, config.WHITE, self.maze_width + 95, 100, self.screen)
        pygame.display.flip()

    """
    Runs the maze on the screen
    """
    def run(self) -> None:
        pygame.display.set_caption(self.maze.maze_size.to_string() + " maze using " + self.player.search_algo_string() + " search")
        self.render()
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_button.handle_event(event):
                        return #go back to menu page
                    elif self.pause_button.handle_event(event) and not self.goal.get_achieved():
                        self.pause_button.toggle(True)
                        self.play_button.toggle(False)
                    elif self.play_button.handle_event(event) and not self.goal.get_achieved():
                        self.pause_button.toggle(False)
                        self.play_button.toggle(True)
                    elif self.play_button.handle_event(event):
                        self.pause_button.toggle(False)
                        self.play_button.toggle(True)
                    if self.search_algorithm_enum != search_algorithm_type.SearchAlgoType.UNIFORM:
                        if not self.analysed and self.search_algorithm_enum != search_algorithm_type.SearchAlgoType.UNIFORM:
                            self.analysis_button.handle_event(event)
                elif event.type == MOVE_AGENTS and not self.goal.get_achieved() and not self.pause_button.get_toggled() and not self.game_lost:
                    print("--- Cycle " + str(self.cycle_count) + " ---")
                    self.cycle()
                    self.cycle_count += 1
                if self.search_algorithm_enum != search_algorithm_type.SearchAlgoType.UNIFORM:
                    if self.analysis_button.get_selected():
                        Analysis.analyse(self.maze, self.player)
                        self.analysed = True
                        self.analysis_button.set_selected(False)
                self.render()

    """
    Completes a cycle of the world, updating and moving players and ghosts
    """
    def cycle(self) -> None:
        world_state = WorldState(self.maze, self.ghosts, self.goal, self.player.get_location())
        self.player.revise(world_state)
        for ghost in self.ghosts:
            ghost.revise(world_state)
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
        if self.player_caught():
            self.game_lost = True
            print("Player has been caught!")
        if self.search_algorithm_enum != search_algorithm_type.SearchAlgoType.UNIFORM:
            if self.analysis_button.get_selected():
                Analysis.analyse(self.maze, self.player)
                self.analysed = True
                self.analysis_button.set_selected(False)
        self.render()

    """
    Find out if any of the ghosts are on the same location as the player
    """
    def player_caught(self) -> bool:
        for ghost in self.ghosts:
            if ghost.get_location() == self.player.get_location() :
                return True
        return False
    
    """
    Update goal if player is at the same location
    """
    def update_goals(self) -> None:
        for goal in self.cupcakes:
            if self.player.get_location() == goal.get_location(): 
                goal.set_achieved()

    """
    Find out of all the goals in the maze have been reached
    """
    def all_goals_achieved(self) -> bool:
        for goal in self.goals:
            if not goal.get_achieved():
                return False
        return True