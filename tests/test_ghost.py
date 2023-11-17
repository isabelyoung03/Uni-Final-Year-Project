import unittest
from src.enums.ghost_behaviour import GhostBehaviour
from src.environment.Goal import Goal
from src.enums.size import MazeSize
from src.environment.Maze import Maze
from src.search_algorithms.breadth_first import BreadthFirstSearch
from src.enums.action import Action
from src.agents.Ghost import Ghost

class TestGhost(unittest.TestCase):
    def test_ghost(self):
        maze = Maze(MazeSize.SMALL)
        ghost = Ghost(1,1, maze, GhostBehaviour.RANDOM)

        ghost.execute(Action.RIGHT)
        self.assertEqual(ghost.x, 2, "New x should be 2")

        ghost.execute(Action.LEFT)
        self.assertEqual(ghost.x, 1, "New x should be 1")

        ghost.execute(Action.DOWN)
        self.assertEqual(ghost.y, 1, "Y should still be 1")

        ghost.execute(Action.UP)
        self.assertEqual(ghost.y, 1, "X should still be 1")

if __name__ == '__main__':
    unittest.main()