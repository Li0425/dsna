from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            pivot = l + (r - l) // 2
            pivot_num = nums[pivot]
            if pivot_num == target:
                return pivot
            elif pivot_num < target:
                l = pivot + 1
            else:
                r = pivot - 1
        return -1
