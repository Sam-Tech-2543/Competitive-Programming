# 403. Frog Jump
# https://leetcode.com/problems/frog-jump/

from functools import cache
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:

        @cache
        def dfs(curr,next):
            if curr==stones[-1]:
                return True
            
            if curr>stones[-1]:
                return False

            ans=False
            for j in [next-1, next, next+1]:
                if j>0 and j+curr in stones:
                    ans = ans or dfs(curr+j,j)

            return ans

        return dfs(0,0)