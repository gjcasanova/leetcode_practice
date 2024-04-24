"""Problem solution."""


class Solution:
    """Wrap the solution."""

    def canJump(self, nums: list[int]) -> bool:
        """Solve the problem."""
        max_jump = 1

        for num in nums[:-1]:
            max_jump = max(max_jump - 1, num)

            if max_jump == 0:
                return False

        return True
