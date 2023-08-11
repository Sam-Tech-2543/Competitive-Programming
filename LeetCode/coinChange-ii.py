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
