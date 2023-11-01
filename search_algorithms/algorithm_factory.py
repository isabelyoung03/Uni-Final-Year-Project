from search_algorithms.Search_algo import SearchAlgorithm
from search_algorithms.a_star import AStarSearch
from search_algorithms.breadth_first import BreadthFirstSearch
from enums.search_algorithm_type import SearchAlgoType
from search_algorithms.depth_first import DepthFirstSearch
from search_algorithms.uniform_cost import UniformCostSearch

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
        elif search_algo_type == SearchAlgoType.A_STAR_VS_GREEDY:
            return BreadthFirstSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.MINIMAX:
            return BreadthFirstSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.EXPECTIMAX:
            return BreadthFirstSearch(maze, goal)