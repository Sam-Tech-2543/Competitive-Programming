# 2616. Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0:
            return 0

        def helper(num):
            i,n=0,0
            while i<len(nums)-1:
                if abs(nums[i]-nums[i+1])<=num:
                    n+=1
                    i+=2
                else:
                    i+=1
                if n==p:
                    return True
            return False

        nums.sort()
        l,r=0,nums[-1]
        ans=nums[-1]

        while l<=r:
            m=(l+r)//2
            if helper(m):
                ans=m
                r=m-1
            else:
                l=m+1

        return ans
