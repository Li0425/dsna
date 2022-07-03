from typing import List
from collections import Counter


class Solution:
    # TC = O(nLogn), SC = O(1)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # TC = O(n), SC = O(n)
    def majorityElement(self, nums):
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)
