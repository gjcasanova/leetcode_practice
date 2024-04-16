"""Problem solution."""


class Solution:
    """Wrap the solution."""

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """Do not return anything, modify nums1 in-place instead."""
        nums1[m:] = n * [float('inf')]
        idx_j = 0

        for idx_i in range(m+n):
            if idx_j >= n:
                break

            if nums1[idx_i] > nums2[idx_j]:
                nums1.insert(idx_i, nums2[idx_j])
                nums1.pop()
                idx_j += 1
