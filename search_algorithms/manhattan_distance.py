from search_algorithms.a_star_heuristic import AStarHeuristic

"""
Return h using Manhattan distance to estimate distance to goal
"""
class ManhattanDistance(AStarHeuristic):
    def get_h(player_x, player_y, goal_x, goal_y):
        return abs(player_x - goal_x) + abs(player_y - goal_y)