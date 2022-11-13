from typing import List


class Solution:
    # a ^ 0 = a
    # a ^ a = 0
    # a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:   
            ans ^= num
        return ans
