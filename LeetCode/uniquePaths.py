# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r = [1] * n

        for i in range(m - 1):
            nr = [1] * n
            for j in range(n - 2, -1, -1):
                nr[j] = r[j] + nr[j + 1]
            r = nr

        return r[0]


s = Solution()

# Input: m = 3, n = 7
# Output: 28
print(s.uniquePaths(3, 7))

# Input: m = 3, n = 2
# Output: 3
print(s.uniquePaths(3, 2))
