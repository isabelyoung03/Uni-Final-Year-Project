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
    def evaluate(self, state, winning_score=1000, losing_score=-1000, oscillation_penalty=-100) -> int:
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
        
        current_state_tuple = (state.get_player_location(), state.get_ghost_locations())
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

        if max_turn:  #player's turn
            max_eval = -math.inf
            for player_move in self.possible_moves(state.get_player_location()):
                new_state = self.result(player_move, state.get_ghost_locations())
                score, _ = self.minimax(new_state, depth - 1, False, visited_states)
                if score > max_eval:
                    max_eval = score
                    best_move = player_move

        else:  #ghost's turn
            min_eval = math.inf
            best_moves = []

            for opponent_move in self.possible_moves(state.get_ghost_locations()[0]):
                new_state = self.result(state.get_player_location(), opponent_move)
                score, _ = self.minimax(new_state, depth - 1, True, visited_states)
                if score < min_eval:
                    min_eval = score
                    best_moves = [opponent_move]
                elif score == min_eval:
                    best_moves.append(opponent_move)

            best_move = best_moves

        visited_states.remove(state)
        return max_eval if max_turn else min_eval, best_move

    """
    Uses the minimax algorithm to get the best move
    """
    def get_best_move(self, player, ghosts, is_player=True):
        depth = 5
        if self.maze.get_maze_size() == MazeSize.MEDIUM:
            depth = 12
        elif self.maze.get_maze_size() == MazeSize.LARGE:
            depth = 12

        self.player = player
        self.ghosts = ghosts
        ghost_locations = []
        for ghost in self.ghosts:
            ghost_locations.append(ghost.get_location())
        current_state = State(player.get_location(), ghost_locations)
        minimax = self.minimax(current_state, depth, is_player)
        best_location = minimax[1]
        return self.get_action_to_location(best_location[0], best_location[1], is_player, current_state)
    
    """
    Get the best moves for the ghosts
    """
    def get_best_moves_for_ghosts(self, player, ghosts):
        depth = 5
        if self.maze.get_maze_size() == MazeSize.MEDIUM:
            depth = 12
        elif self.maze.get_maze_size() == MazeSize.LARGE:
            depth = 12

        self.player = player
        self.ghosts = ghosts
        ghost_locations = []
        for ghost in self.ghosts:
            ghost_locations.append(ghost.get_location())
        current_state = State(player.get_location(), ghost_locations)
        _, best_moves = self.minimax(current_state, depth, True)

        actions = []
        for i in range(len(best_moves)):
            actions.append(self.get_action_to_location(best_moves[i][0], best_moves[i][1], current_state.get_ghost_locations()[i]))
        print(actions)
        return actions

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
        return SearchAlgoType.MINIMAX
    
    def search():
        pass