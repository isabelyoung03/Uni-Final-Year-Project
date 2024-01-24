from src.search_algorithms.minimax import Minimax
from src.search_algorithms.reflex import Reflex
from src.search_algorithms.greedy import GreedySearch
from src.search_algorithms.Search_algo import SearchAlgorithm
from src.search_algorithms.a_star import AStarSearch
from src.search_algorithms.breadth_first import BreadthFirstSearch
from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.depth_first import DepthFirstSearch
from src.search_algorithms.uniform_cost import UniformCostSearch

"""
Factory class for creating a new search algorithm based on the enum and maze supplied
"""
class SearchAlgorithmFactory():
    @staticmethod
    def create_new(search_algo_type, maze, goal) -> SearchAlgorithm:
        if search_algo_type == SearchAlgoType.BREADTH:
            return BreadthFirstSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.DEPTH:
            return DepthFirstSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.UNIFORM:
            return UniformCostSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.A_STAR:
            return AStarSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.A_STAR_ALL_CELLS:
            return AStarSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.GREEDY:
            return GreedySearch(maze, goal)
        elif search_algo_type == SearchAlgoType.MINIMAX:
           return Minimax(maze, goal)
        elif search_algo_type == SearchAlgoType.EXPECTIMAX:
            return BreadthFirstSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.REFLEX:
            return Reflex(maze, goal)