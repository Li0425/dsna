from typing import List


class Solution:
    # TLE solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     max_subarray = -math.inf
    #     for i in range(len(nums)):
    #         curr_subarray = 0
    #         for j in range(i, len(nums)):
    #             curr_subarray += nums[j]
    #             max_subarray = max(max_subarray, curr_subarray)
    #     return max_subarray
    
    # Dynamic programming, Kadane's algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            # we should reset curr to the currently visited number
            # if the currently visited num is larger than the sum of it and the previous subarray
            # e.g. [8,-19,5]. When we visit 5, curr subarray is [8,-19]. Adding 5 to it gets -6, but 5 is bigger than -6
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray