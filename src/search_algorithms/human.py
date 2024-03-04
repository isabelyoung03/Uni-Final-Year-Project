from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm

"""
Placeholder search algorithm for human vs machine
"""
class Human(SearchAlgorithm):
    def __init__(self, maze, goals):
        self.previous_locations = []
        self.maze = maze
        self.goals = goals
        
    """
    Get enum for this search algorithm
    """
    def get_enum(self) -> SearchAlgoType:
        return SearchAlgoType.HUMAN
    
    def search():
        pass
