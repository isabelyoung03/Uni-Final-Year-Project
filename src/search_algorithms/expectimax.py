import math
import random
from src.enums.size import MazeSize
from src.environment.Maze import Maze
from src.environment.Goal import Goal
from src.search_algorithms.a_star import AStarSearch
from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm
from src.enums.action import Action
from src.search_algorithms.minimax_state import State

"""
Expectimax algorithm
"""
class Expectimax(SearchAlgorithm):
    def __init__(self, maze: Maze, cupcake: Goal):
        self.maze = maze
        self.cupcake = cupcake
        self.a_star_search = AStarSearch(maze)
        self.player_oscillation_history = []

    """
    Returns true of the state terminates the game...
    This is true if the player is in the same location as the cupcake or if the opponent
    is in the same location as the player.
    """
    def is_terminal_state(self, state) -> bool:
        if state.get_player_location() == self.cupcake.get_location():
            return True
        for opponent_location in state.get_ghost_locations():
            if opponent_location == state.get_player_location():
                return True
        return False

    """
    Gets the possible moves from a based for either player or opponent
    """
    def possible_moves(self, location) -> list:
        (x, y) = location
        possible_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            if self.maze.check_valid_location(x + dx, y + dy):
                possible_moves.append((x + dx, y + dy))
        return possible_moves

    """
    Return resulting state after player and opponent moves
    """
    def result(self, player_move, opponent_moves: list) -> State:
        return State(player_move, opponent_moves)

    """
    Evaluates a state and returns a score
    """
    def evaluate(self, state, winning_score=1000, losing_score=-1000) -> int:
        player_location = state.get_player_location()
        ghost_locations = state.get_ghost_locations()
        cupcake_location = self.cupcake.get_location() 

        #use A* search to find shortest number of moves from player to goal
        self.a_star_search.set_goal(cupcake_location[0],  cupcake_location[1])
        distance_to_goal = len(self.a_star_search.search(player_location[0], player_location[1]))

        #use A* search to find shortest number of moves from player to all ghosts
        dist_to_all_ghosts = 0
        for ghost_location in ghost_locations:
            self.a_star_search.set_goal(ghost_location[0], ghost_location[1])
            distance_to_ghost = len(self.a_star_search.search(player_location[0], player_location[1]))
            dist_to_all_ghosts += distance_to_ghost

        if state.get_player_location() == cupcake_location:
            return winning_score
        for ghost_location in ghost_locations:
            if ghost_location == state.get_player_location():
                return losing_score
        
        score = distance_to_goal - distance_to_ghost
        return score
    
    """
    Expectimax algorithm function that is used recursively
    """
    def expectimax(self, state: State, depth: int, max_turn: bool, visited_states=None):
        if visited_states is None:
            visited_states = []

        if depth == 0 or self.is_terminal_state(state) or state in visited_states:
            return self.evaluate(state), None

        best_move = None
        visited_states.append(state)

        if max_turn:  #player's turn
            max_eval = -math.inf
            for player_move in self.possible_moves(state.get_player_location()):
                new_ghost_locations = state.get_ghost_locations()
                new_state = self.result(player_move, new_ghost_locations)
                score, _ = self.expectimax(new_state, depth - 1, False, visited_states)
                if score > max_eval:
                    max_eval = score
                    best_move = player_move

        else:  #opponent's turn
            min_eval = math.inf
            best_moves = []

            total_probability = 1.0 / len(state.get_ghost_locations())

            for i, ghost_location in enumerate(state.get_ghost_locations()):
                moves_for_ghost = []

                possible_ghosts_moves = self.possible_moves(ghost_location)
                for opponent_move in possible_ghosts_moves:
                    new_ghost_locations = state.get_ghost_locations().copy()
                    new_ghost_locations[i] = opponent_move
                    new_state = self.result(state.get_player_location(), new_ghost_locations)
                    score, _ = self.expectimax(new_state, depth - 1, True, visited_states)
                    moves_for_ghost.append((score, opponent_move))

                prob = 1.0 / len(possible_ghosts_moves)
                expected_score_for_ghost = sum(prob * score for score, _ in moves_for_ghost) * total_probability
                best_move_for_ghost = (expected_score_for_ghost, moves_for_ghost[0][1]) 

                if best_move_for_ghost[0] < min_eval:
                    min_eval = best_move_for_ghost[0]
                    best_moves = [best_move_for_ghost[1]]
                elif best_move_for_ghost[0] == min_eval:
                    best_moves.append(best_move_for_ghost[1])

            best_move = best_moves

        visited_states.remove(state)
        return max_eval if max_turn else min_eval, best_move

    """
    Uses the minimax algorithm to get the best move
    """
    def get_best_move_for_player(self, player, ghosts):
        depth = self.get_depth(self.maze.get_maze_size(), len(ghosts))
        ghost_locations = []
        for ghost in ghosts:
            ghost_locations.append(ghost.get_location())
        current_state = State(player.get_location(), ghost_locations)
        random_number = random.randint(0, 9)
        if random_number == 0:
            random_move = random.choice(self.possible_moves(player.get_location()))
            print("Player doing random move")
            return self.get_action_to_location(random_move[0], random_move[1], current_state.get_player_location())
        else:
            expectimax = self.expectimax(current_state, depth, True)
            best_location = expectimax[1]
            return self.get_action_to_location(best_location[0], best_location[1], current_state.get_player_location())
    
    """
    Get the best moves for the ghosts
    """
    def get_best_moves_for_ghosts(self, player, ghosts):
        depth = self.get_depth(self.maze.get_maze_size(), len(ghosts))
        ghost_locations = [ghost.get_location() for ghost in ghosts]

        current_state = State(player.get_location(), ghost_locations)
        _, best_moves = self.expectimax(current_state, depth, False)

        actions = []
        for i in range(len(ghost_locations)):
            random_number = random.randint(0, 9)
            if random_number == 0:
                random_move = random.choice(self.possible_moves(ghost_locations[i]))
                actions.append(self.get_action_to_location(random_move[0], random_move[1], ghost_locations[i]))
                print("Ghost doing random move")
            else:
                if best_moves and i < len(best_moves) and best_moves[i] is not None:
                    actions.append(self.get_action_to_location(best_moves[i][0], best_moves[i][1], ghost_locations[i]))
                else:
                    actions.append(Action.IDLE)
        return actions
    
    """
    Get depth used for opponent expectimax, depending on opponent number and maze size
    Necessary because higher depth on 3 opponents in a larger maze causes program to be slow
    """
    def get_depth(self, maze_size, opponent_no) -> int:
        if opponent_no == 1:
            if maze_size == MazeSize.SMALL:
                depth = 10
            elif maze_size == MazeSize.MEDIUM:
                depth = 10
            else:
                depth = 12
        elif opponent_no == 2:
            if maze_size == MazeSize.SMALL:
                depth = 8
            elif maze_size == MazeSize.MEDIUM:
                depth = 9
            else:
                depth = 11
        elif opponent_no == 3:
            if maze_size == MazeSize.SMALL:
                depth = 8
            elif maze_size == MazeSize.MEDIUM:
                depth = 10
            else:
                depth = 10
        return depth

    """
    Get the move needed to go to location i,j from current location
    """
    def get_action_to_location(self, i: int, j: int, current_location):
        (x, y) = current_location
        action = Action.IDLE
        if i - x == 1:
            action = Action.RIGHT
        elif i - x == -1:
            action = Action.LEFT
        elif j - y == 1:
            action = Action.DOWN
        elif j - y == -1:
            action = Action.UP
        return action
    
    """
    Get enum for this search algorithm
    """
    def get_enum(self) -> SearchAlgoType:
        return SearchAlgoType.EXPECTIMAX
    
    def search():
        pass