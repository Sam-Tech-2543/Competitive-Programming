# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [0 for i in range(0, amount + 1)]
        cache[0] = 1

        for i in coins:
            for j in range(i, amount + 1):
                cache[j] += cache[j - i]

        return cache[-1]


s=Solution()

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
print(s.change(5, [1,2,5]))

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
print(s.change(3,[2]))