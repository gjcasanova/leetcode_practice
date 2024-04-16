"""Automatic tests."""

import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    """Test cases."""

    def test_example_1(self):
        """Test case 1."""
        solver = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        solver.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_example_2(self):
        """Test case 2."""
        solver = Solution()
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0

        solver.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_example_3(self):
        """Test case 3."""
        solver = Solution()
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1

        solver.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])


if __name__ == '__main__':
    unittest.main()
