"""Automatic tests."""

import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    """Test cases."""

    def test_example_1(self):
        """Test case 1."""
        solver = Solution()
        nums = [2, 3, 1, 1, 4]

        self.assertEqual(solver.canJump(nums), True)

    def test_example_2(self):
        """Test case 1."""
        solver = Solution()
        nums = [3, 2, 1, 0, 4]

        self.assertEqual(solver.canJump(nums), False)


if __name__ == '__main__':
    unittest.main()
