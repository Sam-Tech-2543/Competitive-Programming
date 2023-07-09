# 15. 3Sum
# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol=[]
        nums.sort()
        for i,a in enumerate(nums):
            l=i+1
            r=len(nums)-1
            while l<r:
                ans=a+nums[l]+nums[r]
                if ans>0:
                    r-=1
                elif ans<0:
                    l+=1
                else:
                    if [a,nums[l],nums[r]] not in sol:
                        sol.append([a,nums[l],nums[r]])
                    l+=1
        
        return sol

s=Solution()

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(s.threeSum([-1,0,1,2,-1,-4]))

# Input: nums = [0,1,1]
# Output: []
print(s.threeSum([0,1,1]))