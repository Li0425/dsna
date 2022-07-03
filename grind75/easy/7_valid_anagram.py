class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count_letters(s: str) -> dict:
            ans = {}
            for c in s:
                if c not in ans:
                    ans[c] = 1
                else:
                    ans[c] = ans[c] + 1
            return ans
        
        s_dict = count_letters(s)
        t_dict = count_letters(t)
        
        return s_dict == t_dict
