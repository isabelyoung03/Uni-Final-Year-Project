import sys

import pygame
from agents.Player import Player
from environment.Maze import Maze
import config
from gui.menu import Menu
from gui.button import Button
from gui.option_button import OptionButton
from gui.button_group import ButtonGroup
from search_algorithms.depth_first import DepthFirstSearch
from environment.world_controller_factory import WorldControllerFactory
from search_algorithms.algorithm_factory import SearchAlgorithmFactory

class MazeSearch:
    def __init__(self):
        pygame.init()
        
    """
    Runs the program
    """
    def run(self):
        while True:
            menu = Menu()
            selected_options = menu.maze_selection_menu()
            maze = selected_options[0]
            search_algorithm_enum = selected_options[1]
            pygame.display.set_caption(maze.maze_size.to_string() + " " + search_algorithm_enum.value +  " Search Maze")
            world_controller = WorldControllerFactory.create_new(maze, 1, 1, search_algorithm_enum)
            world_controller.run()

if __name__ == '__main__':
    maze_search = MazeSearch()
    maze_search.run()