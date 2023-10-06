import pygame
import sys
from gui.button import Button
import config


def hello():
    print("hello")
"""
Displays the maze selection menu and returns the selected maze
"""
def maze_selection_menu():
    pygame.display.set_caption("Menu")
    menu_screen = pygame.display.set_mode((config.MENU_SCREEN_WIDTH, config.MENU_SCREEN_HEIGHT))
    selected_maze = None
    menu_screen.fill(config.BLACK)

    display_text('Single-Agent and Multi-Agent Search in Maze Games', 20, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 50, menu_screen)
    display_text('By Isabel Young', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 125, menu_screen)
    
    display_text('Select maze size', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 200, menu_screen)
    
    small = Button('Small', 20, config.GREEN, config.BLACK, 200, 240, hello)
    medium = Button('Medium', 20, config.PINK, config.BLACK, config.MENU_SCREEN_WIDTH // 2, 240, hello)
    large = Button('Large', 20, config.GREEN, config.BLACK, 400, 240, hello)

    size_buttons = [small, medium, large]
    
    for button in size_buttons:
        button.draw(menu_screen) 
        
    display_text('Select search algorithm', 16, config.WHITE, config.MENU_SCREEN_WIDTH // 2, 315, menu_screen)

    breadth = Button('Breadth-first', 20, config.GREEN, config.BLACK, 150, 355, hello)
    depth = Button('Depth-first', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2, 355, hello)
    uniform = Button('Uniform-cost', 20, config.PINK, config.BLACK, 450, 355, hello)
    greedy_a_star = Button('Greedy vs A*', 20, config.GREEN, config.BLACK, 150, 415, hello)
    minimax = Button('Minimax', 20, config.GREEN, config.BLACK, config.MENU_SCREEN_WIDTH // 2, 415, hello)
    expectimax = Button('Expectimax', 20, config.GREEN, config.BLACK, 450, 415, hello)

    algo_buttons = [breadth, depth, uniform, greedy_a_star, minimax, expectimax]

    for button in algo_buttons:
        button.draw(menu_screen) 

    transformation = (config.SPRITE_WIDTH*config.PIXEL_SCALE, config.SPRITE_HEIGHT*config.PIXEL_SCALE)
    character = pygame.transform.scale(pygame.image.load("gui/resources/Down.png"), transformation)
    menu_screen.blit(character, dest = (config.MENU_SCREEN_WIDTH // 2 - config.SPRITE_WIDTH, 70))

    while selected_maze == None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    selected_maze = config.SMALL_MAZE_MAP
        pygame.display.flip()
    return selected_maze

"""
Display text string on the given screen, of a particular size and colour at location x,y
"""
def display_text(string, font_size, colour, x, y, screen):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(string, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)