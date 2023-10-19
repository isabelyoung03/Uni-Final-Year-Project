from search_algorithms.breadth_first import BreadthFirstSearch
from enums.search_algorithm_type import SearchAlgoType
from search_algorithms.depth_first import DepthFirstSearch
from search_algorithms.uniform_cost import UniformCostSearch

"""
Factory class for creating a new search algorithm based on the enum and maze supplied
"""
class SearchAlgorithmFactory():
    @staticmethod
    def create_new(search_algo_type, maze, goal):
        if search_algo_type == SearchAlgoType.BREADTH:
            return BreadthFirstSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.DEPTH:
            return DepthFirstSearch(maze, goal)
        elif search_algo_type == SearchAlgoType.UNIFORM:
            return UniformCostSearch(maze)
        elif search_algo_type == SearchAlgoType.GREEDY_A_STAR:
            return DepthFirstSearch(maze)
        elif search_algo_type == SearchAlgoType.MINIMAX:
            return DepthFirstSearch(maze)
        elif search_algo_type == SearchAlgoType.EXPECTIMAX:
            return DepthFirstSearch(maze)