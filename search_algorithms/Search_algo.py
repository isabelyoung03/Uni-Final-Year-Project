from abc import ABC, abstractmethod
class SearchAlgorithm(ABC):
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def __init__(self, maze, opponent_locations=None):
        self.maze = maze
        self.opponent_locations = opponent_locations

    """
    Get best move 
    """
    @abstractmethod
    def search(self):
        pass

    """
    Return enum for search algorithm
    """
    @abstractmethod
    def get_enum(self):
        pass 
