import sys

import pygame

class MazeSearch:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        self.image = pygame.image.load("resources/Down.png")
        self.image = pygame.transform.scale(self.image, (21,36))
        self.position = (100,100)
        pygame.display.set_caption("Menu")

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        pygame.display.flip()
        self.screen.blit(self.image, dest = self.position)

if __name__ == '__main__':
    maze_search = MazeSearch()
    maze_search.run_game()