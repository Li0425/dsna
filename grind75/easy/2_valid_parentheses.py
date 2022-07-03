class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []
        
        for c in s:
            if c in bracket_dict:
                complement = stack.pop() if stack else '#'
                if complement != bracket_dict[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack
