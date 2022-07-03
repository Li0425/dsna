from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} # Python implementation of hashmap is dictionary. num: idx
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hm:
                return [idx, hm[complement]]
            hm[num] = idx
