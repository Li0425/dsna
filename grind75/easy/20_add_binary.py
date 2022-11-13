class Solution:
    # Using built-in functions: TC = O(N+M)
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)
        return bin(a_int + b_int)[2:]


    # Bit-by-bit manipulation: TC&SC = O(max(N,M))
    # def addBinary(self, a, b) -> str:
    #     n = max(len(a), len(b))
    #     a, b = a.zfill(n), b.zfill(n)
        
    #     carry = 0
    #     answer = []
    #     for i in range(n - 1, -1, -1):
    #         if a[i] == '1':
    #             carry += 1
    #         if b[i] == '1':
    #             carry += 1
                
    #         if carry % 2 == 1:
    #             answer.append('1')
    #         else:
    #             answer.append('0')
            
    #         carry //= 2
        
    #     if carry == 1:
    #         answer.append('1')
    #     answer.reverse()
        
    #     return ''.join(answer)


    # Bit manipulation: TC = O(N+M), SC = O(max(N,M))
    # XOR: a sum of two binaries without taking carry into account
    # 1^0 = 1, 0^1 = 1, 1^1 = 0, 0^0 = 0
    # def addBinary(self, a, b) -> str:
    #     x, y = int(a, 2), int(b, 2)
    #     while y:
    #         x, y = x ^ y, (x & y) << 1
    #     return bin(x)[2:]
