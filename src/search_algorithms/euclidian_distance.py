import math
from src.search_algorithms.a_star_heuristic import AStarHeuristic

"""
Calculates the Euclidian Distance between two points
"""

class EuclidianDistance(AStarHeuristic):
    """
    Return h using Euclidian distance to estimate distance to goal
    """
    def get_h(player_x, player_y, goal_x, goal_y) -> float:
        return math.sqrt((goal_x - player_x) ** 2 + (goal_y - player_y) ** 2)