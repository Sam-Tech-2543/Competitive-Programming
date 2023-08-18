# 6922. Ways to Express an Integer as Sum of Powers
# https://leetcode.com/contest/biweekly-contest-109/problems/ways-to-express-an-integer-as-sum-of-powers/


class Solution:
    def recursion(self, finalNum, power, currNum):
        ans = finalNum - (currNum**power)
        if ans == 0:
            return 1
        elif ans < 0:
            return 0
        else:
            return self.recursion(ans, power, currNum + 1) + self.recursion(
                finalNum, power, currNum + 1
            )

    def numberOfWays(self, n: int, x: int) -> int:
        return self.recursion(n, n, 0, x)


s = Solution()

# Input: n = 10, x = 2
# Output: 1
n = 10
x = 2
print(s.numberOfWays(n, x))

# Input: n = 100, x = 2
# Output: 3
n = 100
x = 2
print(s.numberOfWays(n, x))
