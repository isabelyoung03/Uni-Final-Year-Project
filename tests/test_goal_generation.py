import hypothesis.strategies as st
from hypothesis import given
from src.environment.Goal import Goal
from src.environment.Goal_factory import GoalFactory
from src.environment.Maze import Maze
from src.enums.size import MazeSize

maze_strategy = st.sampled_from([MazeSize.SMALL, MazeSize.MEDIUM, MazeSize.LARGE])

@given(maze_size=maze_strategy)
def test_generate_goals_in_all_cells(maze_size):
    maze = Maze(maze_size)  
    goals = GoalFactory.generate_goals_in_all_cells(maze)

    assert isinstance(goals, list)
    for goal in goals:
        assert isinstance(goal, Goal) #make sure the list is just goals

    maze_map = maze.get_map()
    goal_cells = sum(row.count(" ") for row in maze_map) #make sure the number of goals in correct
    assert len(goals) == goal_cells