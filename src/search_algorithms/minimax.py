import math
from src.enums.size import MazeSize
from src.environment.Maze import Maze
from src.environment.Goal import Goal
from src.search_algorithms.a_star import AStarSearch
from src.enums.search_algorithm_type import SearchAlgoType
from src.search_algorithms.Search_algo import SearchAlgorithm
from src.enums.action import Action
from src.search_algorithms.minimax_state import State

class Minimax(SearchAlgorithm):
    def __init__(self, maze: Maze, cupcake: Goal):
        self.maze = maze
        self.cupcake = cupcake
        self.a_star_search = AStarSearch(maze)
        self.oscillation_history = []

    """
    Returns true of the state terminates the game...
    This is true if the player is in the same location as the cupcake or if the opponent
    is in the same location as the player.
    """
    def is_terminal_state(self, state) -> bool:
        if state.get_player_location() == self.cupcake.get_location():
            return True
        if state.get_ghost_location() == state.get_player_location():
            return True
        return False

    """
    Gets the possible moves from a based for either player or opponent
    """
    def possible_moves(self, state, player=True) -> list:
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
    def result(self, player_move, opponent_move) -> State:
        return State(player_move, opponent_move)

    """
    Evaluates a state and returns a score
    """
    def evaluate(self, state, winning_score=1000, losing_score=-1000, oscillation_penalty=-100) -> int:
        player_location = state.get_player_location()
        ghost_location = state.get_ghost_location()
        cupcake_location = self.cupcake.get_location() 

        #use A* search to find shortest number of moves from player to goal
        self.a_star_search.set_goal(cupcake_location[0],  cupcake_location[1])
        distance_to_goal = len(self.a_star_search.search(player_location[0], player_location[1]))

        #use A* search to find shortest number of moves from player to ghost
        self.a_star_search.set_goal(ghost_location[0], ghost_location[1])
        distance_to_ghost = len(self.a_star_search.search(player_location[0], player_location[1]))

        if state.get_player_location() == cupcake_location:
            return winning_score
        elif state.get_ghost_location() == state.get_player_location():
            return losing_score
        
        current_state_tuple = (state.get_player_location(), state.get_ghost_location())
        self.oscillation_history.append(current_state_tuple)
        if len(self.oscillation_history) > 3: #only keep last three states in history
            self.oscillation_history.pop(0)  

        if len(set(self.oscillation_history)) < len(self.oscillation_history): #if oscillating
            return oscillation_penalty
        
        score = distance_to_goal - distance_to_ghost
        return score
    
    """
    Minimax algorithm function that is used recursively
    """
    def minimax(self, state: State, depth: int, max_turn: bool, visited_states=None):
        if visited_states is None:
            visited_states = []

        if depth == 0 or self.is_terminal_state(state) or state in visited_states:
            return self.evaluate(state), None

        best_move = None
        visited_states.append(state)

        if max_turn:  # player's turn
            max_eval = -math.inf
            for player_move in self.possible_moves(state):
                new_state = self.result(player_move, state.get_ghost_location())
                score, _ = self.minimax(new_state, depth - 1, False, visited_states)
                if score > max_eval:
                    max_eval = score
                    best_move = player_move

            # print(f"Player's turn - Depth: {depth}, Score: {max_eval}, Best Move: {best_move}, State: {state}")

        else:  # ghost's turn
            min_eval = math.inf
            for opponent_move in self.possible_moves(state, player=False):
                new_state = self.result(state.get_player_location(), opponent_move)
                score, _ = self.minimax(new_state, depth - 1, True, visited_states)
                if score < min_eval:
                    min_eval = score
                    best_move = opponent_move

            # print(f"Ghost's turn - Depth: {depth}, Score: {min_eval}, Best Move: {best_move}, State: {state}")

        visited_states.remove(state)
        return max_eval if max_turn else min_eval, best_move

    """
    Uses the minimax algorithm to get the best move
    """
    def get_best_move(self, player, ghost, is_player=True):
        depth = 5
        if self.maze.get_maze_size() == MazeSize.MEDIUM:
            depth = 12
        elif self.maze.get_maze_size() == MazeSize.LARGE:
            depth = 12

        self.player = player
        self.ghost = ghost
        current_state = State(self.player.get_location(), self.ghost.get_location())
        minimax = self.minimax(current_state, depth, is_player)
        best_location = minimax[1]
        return self.get_action_to_location(best_location[0], best_location[1], is_player, current_state)

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