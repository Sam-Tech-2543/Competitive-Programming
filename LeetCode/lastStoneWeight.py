# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/


from typing import List

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-stone for stone in stones]

        heapq.heapify(stones)
        stones=list(stones)

        while (len(stones)>=2):
            y=heapq.heappop(stones)
            x=heapq.heappop(stones)

            if y<x:
                heapq.heappush(stones,y-x)

        if len(stones)==0:
            return 0

        return stones[0]*-1
    
s=Solution()


# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
print(s.lastStoneWeight([2,7,4,1,8,1]))