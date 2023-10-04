import pygame
import config
import sys

"""
Displays the maze selection menu and returns the selected maze
"""
def maze_selection_menu():
    pygame.display.set_caption("Menu")
    menu_screen = pygame.display.set_mode((config.MENU_SCREEN_WIDTH, config.MENU_SCREEN_HEIGHT))
    selected_maze = None
    menu_screen.fill(config.BLACK)

    title_font = pygame.font.Font('freesansbold.ttf', 20)
    title = title_font.render('Single-Agent and Multi-Agent Search in Maze Games', True, config.WHITE)
    titleRect = title.get_rect()
    titleRect.center = (config.MENU_SCREEN_WIDTH // 2, 50)
    menu_screen.blit(title, titleRect)

    subtitle_font = pygame.font.Font('freesansbold.ttf', 14)
    subtitle = subtitle_font.render('By Isabel Young', True, config.WHITE)
    subtitleRect = subtitle.get_rect()
    subtitleRect.center = (config.MENU_SCREEN_WIDTH // 2, 125)
    menu_screen.blit(subtitle, subtitleRect)

    
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