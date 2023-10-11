from abc import ABC, abstractmethod
class SearchAlgorithm(ABC):
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def __init__(self):
        pass

    # """
    # Get best move 
    # """
    # @abstractmethod
    # def get_next_move(self):
    #     pass
