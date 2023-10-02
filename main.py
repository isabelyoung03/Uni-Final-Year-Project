import sys

import pygame
import mazes

class MazeSearch:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))

        self.sprite = pygame.image.load("resources/Down.png")
        self.sprite = pygame.transform.scale(self.sprite, (21,36))

        squareScale = (48,48)
        self.leaves = pygame.image.load("resources/Leaves.png")
        self.leaves = pygame.transform.scale(self.leaves, squareScale)

        self.path = pygame.image.load("resources/Path.png")
        self.path = pygame.transform.scale(self.path, squareScale)
        
        self.square_size = 50
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
        self.display_maze(mazes.small_maze)

    def display_maze(self, map):
        y = 0
        for i in map:
            x = 0
            char_array = [char for char in i]
            for c in char_array:
                match c:
                    case 'A':
                        self.screen.blit(self.path, dest = (x,y))
                        self.screen.blit(self.sprite, dest = (x+12,y+8))
                    case 'B':
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect(x, y, self.square_size, self.square_size))
                    case 'X':
                        self.screen.blit(self.leaves, dest = (x,y))
                    case '|':
                        self.screen.blit(self.leaves, dest = (x,y))
                    case '-':
                        self.screen.blit(self.leaves, dest = (x,y))
                    case '+':
                        self.screen.blit(self.leaves, dest = (x,y))
                    case _:
                        self.screen.blit(self.path, dest = (x,y))
                x += self.square_size
            y += self.square_size
                

if __name__ == '__main__':
    maze_search = MazeSearch()
    maze_search.run_game()