import sys
import pygame
from src.enums.action import Action
from src.environment.WorldState import WorldState
from src.environment.world_controller import WorldController
import config
from src.gui.icon_buttton import IconButton
from src.gui.menu import display_text

"""
Special world controller for modelling the player as a reflex agent
"""
class HumanWorldController(WorldController):
    def __init__(self, maze, player, ghosts, cupcakes):
        self.maze = maze
        self.player = player
        self.ghosts = ghosts
        self.cupcakes = cupcakes
        self.screen = pygame.display.set_mode((maze.maze_size.get_width(), maze.maze_size.get_height()))
        self.timer = pygame.time.Clock()
        self.movement_delay = 300
        self.maze_width = maze.get_maze_size().get_width() - 200 #200 is the space left over for buttons
        self.home_button = IconButton("Home.png", self.maze_width + 15, 15, 32, 32, True)
        self.cycle_count = 0
        self.game_lost = False

    """
    Get players decision for next action
    """
    def player_decide(self) -> Action:
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_button.handle_event(event):
                        return Action.IDLE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.player.valid_move(Action.LEFT):
                        return Action.LEFT
                    elif event.key == pygame.K_RIGHT and self.player.valid_move(Action.RIGHT):
                        return Action.RIGHT
                    elif event.key == pygame.K_UP and self.player.valid_move(Action.UP):
                        return Action.UP
                    elif event.key == pygame.K_DOWN and self.player.valid_move(Action.DOWN):
                        return Action.DOWN
                elif event.type == pygame.QUIT:
                    sys.exit()
    """
    Find out of all the goals in the maze have been reached
    """
    def all_goals_achieved(self) -> bool:
        for goal in self.cupcakes:
            if not goal.get_achieved():
                return False
        return True

    """
    Update goal if player is at the same location
    """
    def update_goals(self) -> None:
        for goal in self.cupcakes:
            if self.player.get_location() == goal.get_location(): 
                goal.set_achieved()

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
        for goal in self.cupcakes:
            goal.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        if not self.game_lost:
            self.player.draw(self.screen)
        self.home_button.draw(self.screen)

        if self.all_goals_achieved():
            display_text('Goal achieved!', 20, config.WHITE, self.maze_width + 95, 300, self.screen)
            display_text('In ' + str(self.cycle_count) + ' moves', 15, config.WHITE, self.maze_width + 95, 320, self.screen)
        elif self.game_lost:
            display_text('Player loses!', 20, config.WHITE, self.maze_width + 95, 100, self.screen)
        pygame.display.flip()

    """
    Runs the maze on the screen
    """
    def run(self) -> None:
        pygame.display.set_caption("Playing mode ")
        self.update_goals()
        self.render()
        MOVE_AGENTS = pygame.USEREVENT + 1 #event for moving player when it is time
        pygame.time.set_timer(MOVE_AGENTS, self.movement_delay)
        go_home = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif go_home:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home_button.handle_event(event):
                        return #go back to menu page
                elif event.type == MOVE_AGENTS and not self.all_goals_achieved() and not self.game_lost:
                    print("--- Cycle " + str(self.cycle_count) + " ---")
                    go_home = self.cycle()
                    self.cycle_count += 1
                self.render()

    """
    Complete one cycle, updating everyone in the maze
    """
    def cycle(self) -> None:
        world_state = WorldState(self.maze, self.ghosts, self.cupcakes, self.player.get_location())
        self.player.revise(world_state)
        for ghost in self.ghosts:
            ghost.revise(world_state)
        player_action = self.player_decide() #decide players next move
        if player_action == Action.IDLE:
            return True #go back to menu page
        ghost_action = self.ghosts_decide()
        self.player.execute(player_action) 
        self.update_ghosts(ghost_action)
        self.update_goals()
        if self.all_goals_achieved():
            print("Reached goal!")
        if super().player_caught():
            self.game_lost = True
            print("Player has been caught!")
        self.render()