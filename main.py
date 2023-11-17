import sys

import pygame
from src.agents.Player import Player
from src.environment.Maze import Maze
import config
from src.gui.menu import Menu
from src.gui.button import Button
from src.gui.option_button import OptionButton
from src.gui.button_group import ButtonGroup
from src.search_algorithms.depth_first import DepthFirstSearch
from src.environment.world_controller_factory import WorldControllerFactory
from src.search_algorithms.algorithm_factory import SearchAlgorithmFactory

class MazeSearch:
    def __init__(self):
        pygame.init()
        
    """
    Runs the program
    """
    def run(self):
        while True:
            while True:
                menu = Menu()
                selected_options = menu.maze_selection_menu()
                maze = selected_options[0]
                search_algorithm_enum = selected_options[1]
                world_controller = WorldControllerFactory.create_new(maze, search_algorithm_enum)
                if world_controller.run(): #if world_controller returns...
                    break #go back to menu page

if __name__ == '__main__':
    maze_search = MazeSearch()
    maze_search.run()