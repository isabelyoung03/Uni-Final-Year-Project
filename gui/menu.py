import pygame
import sys
from gui.button import Button
from gui.button_group import ButtonGroup
import config

class Menu:
    def __init__(self):
        self.small = Button('Small', 20, config.GREEN, config.BLACK, 200, 240)
        self.medium = Button('Medium', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2, 240)
        self.large = Button('Large', 20, config.GREEN, config.BLACK, 400, 240)

        self.size_button_group = ButtonGroup([self.small, self.medium, self.large])

        self.menu_screen = pygame.display.set_mode((config.MENU_SCREEN_WIDTH, config.MENU_SCREEN_HEIGHT))

    """
    Displays the maze selection menu and returns the selected maze
    """
    def maze_selection_menu(self):
        pygame.display.set_caption("Menu")
        selected_maze = None
            
        self.display_text('Select search algorithm', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 315, self.menu_screen)

        # breadth = Button('Breadth-first', 20, config.GREEN, config.BLACK, 150, 355)
        # depth = Button('Depth-first', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2, 355)
        # uniform = Button('Uniform-cost', 20, config.GREEN, config.BLACK, 450, 355)
        # greedy_a_star = Button('Greedy vs A*', 20, config.GREEN, config.BLACK, 150, 415)
        # minimax = Button('Minimax', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2, 415)
        # expectimax = Button('Expectimax', 20, config.GREEN, config.BLACK, 450, 415)

        # algo_buttons = [breadth, depth, uniform, greedy_a_star, minimax, expectimax]

        # for button in algo_buttons:
        #     button.draw(self.menu_screen) 

        start_button = Button('Start', 20, config.BLACK, config.WHITE, 250, 480, 100, 50)
        start_button.draw(self.menu_screen)

        transformation = (config.SPRITE_WIDTH*config.PIXEL_SCALE, config.SPRITE_HEIGHT*config.PIXEL_SCALE)
        character = pygame.transform.scale(pygame.image.load("gui/resources/Down.png"), transformation)
        self.menu_screen.blit(character, dest = (config.MENU_SCREEN_WIDTH // 2 - config.SPRITE_WIDTH, 70))

        while selected_maze == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        selected_maze = config.SMALL_MAZE_MAP
                # for button in algo_buttons:
                #     button.handle_event(event)
            # menu_screen.fill(config.BLACK)
            # for button in algo_buttons:
            #     button.draw(menu_screen)
            self.draw()
            pygame.display.flip()
        return selected_maze

    """
    Display text string on the given screen, of a particular size and colour at location x,y
    """
    def display_text(self, string, font_size, colour, x, y, screen):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(string, True, colour)
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    def draw(self):
        self.menu_screen.fill(config.BLACK)

        self.display_text('Single-Agent and Multi-Agent Search in Maze Games', 20, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 50, self.menu_screen)
        self.display_text('By Isabel Young', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 125, self.menu_screen)
        
        self.display_text('Select maze size', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 200, self.menu_screen)

        self.size_button_group.draw(self.menu_screen)