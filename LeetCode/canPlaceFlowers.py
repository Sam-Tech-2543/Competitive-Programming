# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans=0

        flowerbed=[0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                ans+=1

        return ans>=n

        # i=0
        # ans=0
        # while i<len(flowerbed):
        #     if ans==n:
        #         return True
            
        #     if flowerbed[i]==1:
        #         i+=2
        #     elif flowerbed[i]==0:
        #         if i==len(flowerbed)-1 or flowerbed[i+1]==0:
        #             i+=2
        #             ans+=1
        #         else:
        #             i+=3

        # return ans==n

s=Solution()

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
print(s.canPlaceFlowers([1,0,0,0,1],1))

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
print(s.canPlaceFlowers([1,0,0,0,1],2))

# Input: flowerbed = [1,0,0,0,0,1], n = 2
# Output: False
print(s.canPlaceFlowers([1,0,0,0,0,1],2))

# Input: flowerbed = [0,0,0], n = 2
# Output: True
print(s.canPlaceFlowers([0,0,0],2))