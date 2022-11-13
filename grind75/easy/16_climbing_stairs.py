class Solution:
    # The solution I came up with: recursion with memoization
    def __init__(self):
        self.memory = {}
    
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        if n-1 not in self.memory:
            self.memory[n-1] = self.climbStairs(n-1)
        a = self.memory.get(n-1)
            
        if n-2 not in self.memory:
            self.memory[n-2] = self.climbStairs(n-2)
        b = self.memory.get(n-2)
        
        return a + b
