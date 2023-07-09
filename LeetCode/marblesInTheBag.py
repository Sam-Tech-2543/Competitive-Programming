# 2551. Put Marbles in Bags
# https://leetcode.com/problems/put-marbles-in-bags/

from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs=[]
        for i in range(0,len(weights)-1):
            pairs.append(weights[i]+weights[i+1])

        pairs.sort()

        minVal,maxVal=0,0
        for i in range(0,k-1):
            minVal+=pairs[i]
            maxVal+=pairs[len(pairs)-i-1]

        return maxVal-minVal
    

s=Solution()
print(s.putMarbles([1,2,3,4],3))