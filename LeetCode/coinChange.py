# 322. Coin Change
# https://leetcode.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount + 1 for i in range(amount + 1)]
        cache[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - coin])

        return cache[amount] if cache[amount] != amount + 1 else -1


s = Solution()

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
print(s.coinChange([1, 2, 5], 11))

# Input: coins = [2], amount = 3
# Output: -1
print(s.coinChange([1, 2, 5], 11))
