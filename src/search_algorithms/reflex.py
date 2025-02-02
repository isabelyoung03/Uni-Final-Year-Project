from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm

"""
Search algorithm used for reflex agents
"""
class Reflex(SearchAlgorithm):
    def __init__(self, maze, goals):
        self.previous_locations = []
        self.maze = maze
        self.goals = goals
        
    """
    Get enum for this search algorithm
    """
    def get_enum(self) -> SearchAlgoType:
        return SearchAlgoType.REFLEX
    
    def search():
        pass
