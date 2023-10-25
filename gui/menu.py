import pygame
import sys
from agents.Player import Player
from enums.search_algorithm_type import SearchAlgoType
from enums.size import MazeSize
from environment.Maze import Maze
from gui.button import Button
from gui.button_group import ButtonGroup
import config
from gui.option_button import OptionButton

class Menu:
    def __init__(self):
        small = OptionButton('Small', 20, config.GREEN, config.BLACK, 140, 240, MazeSize.SMALL)
        medium = OptionButton('Medium', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2 - 40, 240, MazeSize.MEDIUM)
        large = OptionButton('Large', 20, config.GREEN, config.BLACK, 400, 240, MazeSize.LARGE)

        self.size_button_group = ButtonGroup([small, medium, large])

        breadth = OptionButton('Breadth-first', 20, config.GREEN, config.BLACK, 90, 355, SearchAlgoType.BREADTH)
        depth = OptionButton('Depth-first', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2 - 50, 355, SearchAlgoType.DEPTH)
        uniform = OptionButton('Uniform-cost', 20, config.GREEN, config.BLACK, 400, 355, SearchAlgoType.UNIFORM)
        a_star = OptionButton('A*', 20, config.GREEN, config.BLACK, 140, 415, SearchAlgoType.A_STAR)
        greedy_a_star = OptionButton('A* vs Greedy', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2 - 60, 415, SearchAlgoType.A_STAR_VS_GREEDY)
        minimax = OptionButton('Minimax', 20, config.GREEN, config.BLACK, 420, 415, SearchAlgoType.MINIMAX)
        expectimax = OptionButton('Expectimax', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2 - 60, 475, SearchAlgoType.EXPECTIMAX)

        self.algo_button_group = ButtonGroup([breadth, depth, uniform, a_star, greedy_a_star, minimax, expectimax])

        self.start_button = Button('Start', 20, config.BLACK, config.WHITE, 250, 540, 100, 50)

        self.menu_screen = pygame.display.set_mode((config.MENU_SCREEN_WIDTH, config.MENU_SCREEN_HEIGHT))

    """
    Displays the maze selection menu and returns the selected maze size and search algorithm
    """
    def maze_selection_menu(self):
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
                        maze = Maze(selected_maze_size)
                self.size_button_group.handle_event(event)
                self.algo_button_group.handle_event(event)
            self.draw()
            pygame.display.flip()
        return (maze, selected_search_algo)

    """
    Draw the menu screen
    """
    def draw(self):
        self.menu_screen.fill(config.BLACK)

        transformation = (config.SPRITE_WIDTH*config.PIXEL_SCALE, config.SPRITE_HEIGHT*config.PIXEL_SCALE)
        character = pygame.transform.scale(pygame.image.load("gui/resources/Down.png"), transformation)
        self.menu_screen.blit(character, dest = (config.MENU_SCREEN_WIDTH // 2 - config.SPRITE_WIDTH, 70))

        display_text('Single-Agent and Multi-Agent Search in Maze Games', 20, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 50, self.menu_screen)
        display_text('By Isabel Young', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 125, self.menu_screen)
        display_text('Select maze size', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 200, self.menu_screen)
        display_text('Select search algorithm', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 315, self.menu_screen)
        
        self.size_button_group.draw(self.menu_screen)
        self.algo_button_group.draw(self.menu_screen)

        self.start_button.draw(self.menu_screen)

"""
Display text string on the given screen, of a particular size and colour at location x,y
"""
def display_text(string, font_size, colour, x, y, screen):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(string, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)