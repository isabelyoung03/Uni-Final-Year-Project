import sys

import pygame
from agents.Player import Player
from environment.Maze import Maze
import config
from gui.menu import Menu
from gui.button import Button
from gui.option_button import OptionButton
from gui.button_group import ButtonGroup
from world_controller import WorldController

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
            search_algorithm = selected_options[1]
            player = Player(1,1, maze.map)
            world_controller = WorldController(maze, player)
            world_controller.run()

if __name__ == '__main__':
    maze_search = MazeSearch()
    maze_search.run()