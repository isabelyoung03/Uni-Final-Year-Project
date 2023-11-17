import unittest
from src.environment.Goal import Goal
from src.enums.size import MazeSize
from src.environment.Maze import Maze
from src.search_algorithms.breadth_first import BreadthFirstSearch
from src.enums.action import Action
from src.agents.Player import Player

class TestPlayer(unittest.TestCase):
    def test_player(self):
        maze = Maze(MazeSize.SMALL)
        search = BreadthFirstSearch(maze, [Goal(5,2)])
        player = Player(5,1, search)

        self.assertEqual(player.search_algo_string(), 'Breadth-First', "Search algorithm should be 'Breadth-First''")
        
        player.execute(Action.DOWN)
        self.assertEqual(player.y, 2, "New y should be 2")

        player.execute(Action.UP)
        self.assertEqual(player.y, 1, "New y should be 1")

        player.execute(Action.RIGHT)
        self.assertEqual(player.x, 6, "New x should be 6")

        player.execute(Action.LEFT)
        self.assertEqual(player.x, 5, "New x should be 5")
        
if __name__ == '__main__':
    unittest.main()