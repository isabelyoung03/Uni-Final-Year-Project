import math
from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm
from src.enums.action import Action
from src.search_algorithms.minimax_state import State

class Minimax(SearchAlgorithm):
    def __init__(self, maze, cupcake):
        self.maze = maze
        self.cupcake = cupcake

    """
    Returns true of the state terminates the game...
    This is true if the player is in the same location as the cupcake or if the opponent
    is in the same location as the player.
    """
    def is_terminal_state(self, state):
        if state.get_player_location() == self.cupcake.get_location():
            return True
        if state.get_ghost_location() == state.get_player_location():
            return True
        return False

    """
    Gets the possible moves from a based for either player or opponent
    """
    def possible_moves(self, state, player=True):
        possible_moves = []
        if player:
            (x, y) = state.get_player_location()
        else:
            (x, y) = state.get_ghost_location()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            if self.maze.check_valid_location(x + dx, y + dy):
                possible_moves.append((x + dx, y + dy))
        return possible_moves

    """
    Return resulting state after player and opponent moves
    """
    def result(self, player_move, opponent_move):
        return State(player_move, opponent_move)

    """
    Evaluates a state and returns a score
    """
    def evaluate(self, state, winning_score=1000, losing_score=-1000):
        player_location = state.get_player_location()
        ghost_location = state.get_ghost_location()
        cupcake_location = self.cupcake.get_location() 

        distance_to_goal = abs(player_location[0] - cupcake_location[0]) + abs(player_location[1] - cupcake_location[1])

        distance_to_ghost = abs(player_location[0] - ghost_location[0]) + abs(player_location[1] - ghost_location[1])

        if state.get_player_location() == cupcake_location:
            return winning_score
        elif state.get_ghost_location() == state.get_player_location():
            return losing_score

        score = distance_to_goal - distance_to_ghost

        return score
    
    """
    Minimax algorithm function that is used recursively
    """
    def minimax(self, state: State, depth: int, max_turn: bool, visited_states=None):
        if visited_states is None:
            visited_states = set()

        if depth == 0 or self.is_terminal_state(state) or state in visited_states:
            return self.evaluate(state), None

        best_move = None
        visited_states.add(state)

        if max_turn:  #player's turn
            max_eval = -math.inf
            for player_move in self.possible_moves(state):
                for opponent_move in self.possible_moves(state, False):
                    new_state = self.result(player_move, opponent_move)
                    score, _ = self.minimax(new_state, depth - 1, False, visited_states)
                    if score > max_eval:
                        max_eval = score
                        best_move = (player_move, opponent_move)

            print(f"Player's turn - Depth: {depth}, Score: {max_eval}, Best Move: {best_move}, State: {state}")

        else:  #ghost's turn
            min_eval = math.inf
            for player_move in self.possible_moves(state):
                for opponent_move in self.possible_moves(state, False):
                    new_state = self.result(player_move, opponent_move)
                    score, _ = self.minimax(new_state, depth - 1, True, visited_states)
                    if score < min_eval:
                        min_eval = score
                        best_move = (player_move, opponent_move)

            print(f"Ghost's turn - Depth: {depth}, Score: {min_eval}, Best Move: {best_move}, State: {state}")

        visited_states.remove(state)
        return max_eval if max_turn else min_eval, best_move

    """
    Uses the minimax algorithm to get the best move
    """
    def get_best_move(self, player, ghost, is_player=True):
        self.player = player
        self.ghost = ghost
        current_state = State(self.player.get_location(), self.ghost.get_location())
        minimax = self.minimax(current_state, 10, is_player)

        best_moves = minimax[1]
        print(minimax[0])
        if minimax[1] is not None:
            if is_player:
                best_location = best_moves[0]
                print("player best move", best_location)
            else:
                best_location = best_moves[1]
                print("ghost best move", best_location)
            return self.get_action_to_location(best_location[0], best_location[1], is_player, current_state)
        else:
            return Action.IDLE

    """
    Get the move needed to go to location i,j from current location
    """
    def get_action_to_location(self, i: int, j: int, player: bool, current_state: State):
        if player:
            (x, y) = current_state.get_player_location()
        else:
            (x, y) = current_state.get_ghost_location()
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
        return SearchAlgoType.MINIMAX
    
    def search():
        pass

    
