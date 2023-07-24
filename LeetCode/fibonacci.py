# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1

        ans=0
        n1=0
        n2=1

        for i in range(n-1):
            ans=n1+n2
            n1=n2
            n2=ans

        return ans


s=Solution()


# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
print(s.fib(2))

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
print(s.fib(4))

print(s.fib(6))
