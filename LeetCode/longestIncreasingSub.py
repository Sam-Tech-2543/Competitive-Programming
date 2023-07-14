# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dict={}
        ans=0

        for i in nums:
            maxVal=0
            for j in dict.keys():
                if j<i:
                    maxVal=max(dict.get(j),maxVal)
            dict[i]=1+maxVal
            ans=max(ans,dict[i])
        return ans
    
s=Solution()

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))

# Input: nums = [0,1,0,3,2,3]
# Output: 4
print(s.lengthOfLIS([0,1,0,3,2,3]))

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
print(s.lengthOfLIS([7,7,7,7,7,7,7]))