# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/description/

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        hashMap=dict()
        l,c=0,0

        for i in range(len(nums)-1,-1,-1):
            maxLen,maxCount=1,1

            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    length,count=hashMap[j]
                    if length+1>maxLen:
                        maxLen=length+1
                        maxCount=count
                    elif length+1==maxLen:
                        maxCount+=count
            
            if maxLen>l:
                l=maxLen
                c=maxCount
            elif maxLen==l:
                c+=maxCount

            hashMap[i]=[maxLen,maxCount]

        return c
    
s=Solution()

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
print(s.findNumberOfLIS([1,3,5,4,7]))
