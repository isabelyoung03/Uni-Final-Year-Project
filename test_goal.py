import unittest

from environment.Goal import Goal

class TestGoal(unittest.TestCase):
    def test_goal(self):
        goal = Goal(5,2)
        self.assertEqual(goal.get_achieved(), False, "Goal should not be achieved)")
        self.assertEqual(goal.get_location(), (5,2), "Should be (5,2)")
        goal.set_achieved()
        self.assertEqual(goal.get_achieved(), True, "Goal should be achieved)")

if __name__ == '__main__':
    unittest.main()