from abc import abstractmethod
"""
Class for A star heurisitic functions for h
"""
class AStarHeuristic:
    @abstractmethod
    def get_h(self):
        pass