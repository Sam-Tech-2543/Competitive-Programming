# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]



s=Solution()

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
print(s.twoSum([2,7,11,15],9))

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
print(s.twoSum([3,2,4],6))

# Input: nums = [3,3], target = 6
# Output: [0,1]
print(s.twoSum([3,3],6))