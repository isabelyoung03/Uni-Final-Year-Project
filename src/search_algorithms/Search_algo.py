from abc import ABC, abstractmethod
class SearchAlgorithm(ABC):
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def __init__(self, maze, goals):
        self.maze = maze
        self.goals = goals

    """
    Get path plan
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
