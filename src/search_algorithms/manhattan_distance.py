from src.search_algorithms.a_star_heuristic import AStarHeuristic

"""
Calculates the Manhattan Distance between two points
"""
class ManhattanDistance(AStarHeuristic):
    """
    Return h using Manhattan distance to estimate distance to goal
    """
    def get_h(player_x, player_y, goal_x, goal_y) -> float:
        return abs(player_x - goal_x) + abs(player_y - goal_y)