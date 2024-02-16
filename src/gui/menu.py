import pygame
import sys
from src.agents.Player import Player
from src.enums.search_algorithm_type import SearchAlgoType
from src.enums.size import MazeSize
from src.environment.Maze import Maze
from src.gui.button import Button
from src.gui.button_group import ButtonGroup
import config
from src.gui.option_button import OptionButton

class Menu:
    def __init__(self):
        small = OptionButton('Small', 20, config.GREEN, config.BLACK, 140, 240, MazeSize.SMALL)
        medium = OptionButton('Medium', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2 - 40, 240, MazeSize.MEDIUM)
        large = OptionButton('Large', 20, config.GREEN, config.BLACK, 400, 240, MazeSize.LARGE)
        self.size_button_group = ButtonGroup([small, medium, large])

        maze1 = OptionButton('1', 20, config.GREEN, config.BLACK, 95, 570, 1)
        maze2 = OptionButton('2', 20, config.GREEN, config.BLACK, 125, 570, 2)
        maze3 = OptionButton('3', 20, config.GREEN, config.BLACK, 155, 570, 3)
        self.maze_group = ButtonGroup([maze1, maze2, maze3])

        breadth = OptionButton('Breadth-first', 20, config.GREEN, config.BLACK, 85, 355, SearchAlgoType.BREADTH)
        depth = OptionButton('Depth-first', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2 - 50, 355, SearchAlgoType.DEPTH)
        uniform = OptionButton('Uniform-cost', 20, config.GREEN, config.BLACK, 400, 355, SearchAlgoType.UNIFORM)
        a_star = OptionButton('A*', 20, config.GREEN, config.BLACK, 125, 415, SearchAlgoType.A_STAR)
        a_star_all_cells = OptionButton('A* (goals in all)', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2 - 70, 415, SearchAlgoType.A_STAR_ALL_CELLS)
        greedy = OptionButton('Greedy', 20, config.GREEN, config.BLACK, 430, 415, SearchAlgoType.GREEDY)
        minimax = OptionButton('Minimax', 20, config.GREEN, config.BLACK, 90, 475, SearchAlgoType.MINIMAX)
        expectimax = OptionButton('Expectimax', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2 - 60, 475, SearchAlgoType.EXPECTIMAX)
        reflex = OptionButton('Reflex', 20, config.GREEN, config.BLACK, 435, 475, SearchAlgoType.REFLEX)
        self.algo_button_group = ButtonGroup([breadth, depth, uniform, a_star, a_star_all_cells, greedy, minimax, expectimax, reflex])

        one = OptionButton('1', 20, config.GREEN, config.BLACK, 95, 570, 1)
        two = OptionButton('2', 20, config.GREEN, config.BLACK, 125, 570, 2)
        three = OptionButton('3', 20, config.GREEN, config.BLACK, 155, 570, 3)
        self.opponent_button_group = ButtonGroup([one, two, three])

        self.start_button = Button('Start', 20, config.BLACK, config.WHITE, 250, 540, 100, 50)
        self.menu_screen = pygame.display.set_mode((config.MENU_SCREEN_WIDTH, config.MENU_SCREEN_HEIGHT))

    """
    Displays the maze selection menu and returns the selected maze size and search algorithm
    """
    def maze_selection_menu(self) -> None:
        pygame.display.set_caption("Menu")
        maze = None

        while maze == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.rectangle.collidepoint(event.pos): #if start button is pressed
                        selected_maze_size = self.size_button_group.get_result()
                        selected_search_algo = self.algo_button_group.get_result()
                        no_of_opponents = self.opponent_button_group.get_result()
                        maze_number = self.maze_group.get_result()
                        if selected_maze_size == MazeSize.SMALL and selected_search_algo == SearchAlgoType.MINIMAX or selected_search_algo == SearchAlgoType.EXPECTIMAX:
                            maze = Maze(selected_maze_size, the_map=config.SMALL_MAZE_MAP_4)
                        else:
                            maze = Maze(selected_maze_size, map_number=maze_number)

                self.size_button_group.handle_event(event)
                self.algo_button_group.handle_event(event)
                self.opponent_button_group.handle_event(event)
                self.maze_group.handle_event(event)
            self.draw()
            pygame.display.flip()
        return (maze, selected_search_algo, no_of_opponents)

    """
    Draw the menu screen
    """
    def draw(self) -> None:
        self.menu_screen.fill(config.BLACK)

        transformation = (config.SPRITE_WIDTH*config.PIXEL_SCALE, config.SPRITE_HEIGHT*config.PIXEL_SCALE)
        character = pygame.transform.scale(pygame.image.load("src/gui/resources/Down.png"), transformation)
        self.menu_screen.blit(character, dest = (config.MENU_SCREEN_WIDTH // 2 - config.SPRITE_WIDTH, 70))

        display_text('Single-Agent and Multi-Agent Search in Maze Games', 20, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 50, self.menu_screen)
        display_text('By Isabel Young', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 125, self.menu_screen)
        display_text('Select maze size', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 200, self.menu_screen)
        display_text('Select agent type', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 315, self.menu_screen)

        self.size_button_group.draw(self.menu_screen)
        self.algo_button_group.draw(self.menu_screen)

        self.start_button.draw(self.menu_screen)

        selected_algo = self.algo_button_group.get_result()
        if selected_algo in [SearchAlgoType.MINIMAX, SearchAlgoType.EXPECTIMAX]:
            display_text('Opponents', 16, config.WHITE, 132, 550, self.menu_screen)
            self.opponent_button_group.draw(self.menu_screen)

        if selected_algo in [SearchAlgoType.GREEDY, SearchAlgoType.A_STAR_ALL_CELLS]:
            display_text('Maze', 16, config.WHITE, 132, 550, self.menu_screen)
            self.maze_group.draw(self.menu_screen)

"""
Display text string on the given screen, of a particular size and colour at location x,y
"""
def display_text(string: str, font_size: int, colour, x:int, y:int, screen):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(string, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)