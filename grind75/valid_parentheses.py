class Solution:
    def isValid(self, s: str) -> bool:
        container = []
        left_partner = {')': '(', '}': '{', ']': '['}
        for par in s:
            if len(container) > 0:
                if left_partner.get(par) == container[len(container)-1]:
                    container.pop(len(container)-1)
                else:
                    container.append(par)
            else:
                container.append(par)
        print(container)
        if len(container) > 0:
            return False
        return True