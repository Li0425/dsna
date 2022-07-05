# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(i: int):
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            pivot = l + (r - l) // 2
            if isBadVersion(pivot):
                r = pivot - 1
            else:
                l = pivot + 1
        return l
