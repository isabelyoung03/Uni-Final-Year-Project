
import pygame
from src.gui.menu import Menu
from src.environment.world_controller_factory import WorldControllerFactory

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
                no_of_opponents = selected_options[2]
                world_controller = WorldControllerFactory.create_new(maze, search_algorithm_enum, no_of_opponents)
                if world_controller.run(): #if world_controller returns...
                    break #go back to menu page

if __name__ == '__main__':
    maze_search = MazeSearch()
    maze_search.run()