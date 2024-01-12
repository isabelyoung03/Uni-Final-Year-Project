import math
from src.enums.search_algorithm_type import SearchAlgoType
from src.environment.Goal import Goal
from src.search_algorithms.Search_algo import SearchAlgorithm
from src.search_algorithms.node import Node

"""
Search algorithm used for reflex agents
"""
class Reflex(SearchAlgorithm):
    def __init__(self, maze, goals):
        pass
    """
    Get enum for this search algorithm
    """
    def get_enum(self) -> SearchAlgoType:
        return SearchAlgoType.REFLEX
