from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = int((1 + len(nums)) * len(nums) / 2)
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    # def missingNumber(self, nums: List[int]) -> int:
    #     missing = len(nums)
    #     for i, num in enumerate(nums):
    #         missing ^= i ^ num
    #     return missing
