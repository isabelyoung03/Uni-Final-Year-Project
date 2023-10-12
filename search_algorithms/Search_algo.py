from abc import ABC, abstractmethod
class SearchAlgorithm(ABC):
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def __init__(self, maze):
        self.maze = maze

    """
    Get best move 
    """
    @abstractmethod
    def search(self):
        pass
