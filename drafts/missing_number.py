class Solution:
    def missingNumber(self, nums) -> int:
        nums.sort()
        a = 0
        
        for i in range(0, len(nums)):
            if nums[i] + 1 != nums[i+1]:
                a = nums[i] + 1
                i += 1
            else:
                i += 1
                if nums[i] == nums[-1]:
                    a = nums[-1] + 1
        return a

s = Solution()
result = s.missingNumber([3,0,4,2,6,1])
print(result)
result = s.missingNumber([0])
print(result)