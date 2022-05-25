from typing import List


class Solution:
    def two_sum(self, num_list, target):
        result = set()
        hm = {}
        for idx, num in enumerate(num_list):
            if target-num not in hm:
                hm[num] = idx     
            else:
                other_idx = hm[target-num]
                result.add((idx, other_idx))
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for idx, num in enumerate(nums):
            remaining_nums = nums.copy()
            remaining_nums.pop(idx)
            two_sum_results = self.two_sum(remaining_nums, 0-num)
            if two_sum_results:
                for pair in two_sum_results:
                    ans.append([num, remaining_nums[pair[0]], remaining_nums[pair[1]]])

        return ans

    def process_result(self, result):
        sets = set(map(lambda x: tuple(sorted(x)), result))
        ans = []
        for item in sets:
            ans.append([item[0], item[1], item[2]])
        return ans

input = [-1,0,1,2,-1,-4]
s = Solution()
result = s.threeSum(input)
print(f"result: {result}")
print('-----')
print(f"processed: {s.process_result(result)}")
