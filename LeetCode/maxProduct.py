# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxVal=float('-inf')
        # for i in range(len(nums)):
        #     ans=1
        #     for j in range(i,len(nums)):
        #         ans*=nums[j]
        #         maxVal=max(ans,maxVal)

        # return maxVal

        ans=float('-inf')

        # Prefix 
        temp=1
        for i in range(len(nums)):
            if nums[i]==0:
                temp=1
                ans=max(ans,0)
                continue
            temp*=nums[i]
            ans=max(ans,temp)

        # Suffix 
        temp=1
        for i in range(len(nums)-1, -1, -1):
            if nums[i]==0:
                temp=1
                ans=max(ans,0)
                continue
            temp*=nums[i]
            ans=max(ans,temp)
        
        return ans

        