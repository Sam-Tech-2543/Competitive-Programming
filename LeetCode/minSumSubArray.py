# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List
import sys

class Solution:
    def minSubArrayLen_BruteForce(self, target: int, nums: List[int]) -> int:
        l=len(nums)
        flag=0
        ans=sys.maxsize
        i=0
        for i in range(0,l+1):
            for j in range(0,i):
                # print(nums[j:i])
                lst=nums[j:i]
                if sum(lst)>=target:
                    t=i-j
                    if t<ans:
                        ans=t
                        flag=1
        
        if flag:
            return ans
        return 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        ans=float('inf')

        l=0
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target and l<=r:
                ans=min(r-l+1,ans)
                s-=nums[l]
                l+=1

        return 0 if ans==float('inf') else ans


s=Solution()

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2   
print(s.minSubArrayLen(7,[1,2,3,4]))

# Input: target = 4, nums = [1,4,4]
# Output: 1
print(s.minSubArrayLen(4,[1,4,4]))

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
print(s.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))
