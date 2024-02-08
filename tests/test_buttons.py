import pygame
import config

from src.environment.Maze import Maze
from src.gui.menu import Menu
from src.enums.search_algorithm_type import SearchAlgoType

import pytest

"""
Tests the results of the menu page
"""
@pytest.mark.parametrize(
    "allowed_opponents",
    [
        ([1, 2, 3]),
    ]
)
def test_maze_selection_menu(allowed_opponents):
    pygame.init()
    menu = Menu()
    result = menu.maze_selection_menu()

    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], Maze)
    assert isinstance(result[1], SearchAlgoType)
    assert result[2] in allowed_opponents

    pygame.quit()