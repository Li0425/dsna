from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        letters = Counter(magazine) 
        
        for c in ransomNote:
            if not letters.get(c):
                return False
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        
        return True
    
    # My solution:
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     def count_char_in_string(s: str) -> dict:
    #         ans = {}
    #         for c in s:
    #             if c in ans:
    #                 ans[c] = ans[c] + 1
    #             else:
    #                 ans[c] = 1
    #         return ans
        
    #     r_hm = count_char_in_string(ransomNote)
    #     m_hm = count_char_in_string(magazine)
        
    #     for k, v in r_hm.items():
    #         m_char = m_hm.get(k)
    #         if not m_char:
    #             return False
    #         if m_char < v:
    #             return False
        
    #     return True