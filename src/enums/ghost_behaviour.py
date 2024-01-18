from enum import Enum
"""
Enum for the behaviour of a ghost
"""
class GhostBehaviour(Enum):
    RANDOM_CHASE = 1
    RANDOM = 2
    INTELLIGENT = 3