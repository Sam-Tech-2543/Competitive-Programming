# 268. Missing Number
# https://leetcode.com/problems/missing-number/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t1,t2=0,0
        size=len(nums)
        for i in range(size):
            t1+=nums[i]
            t2+=i
        
        t2+=size

        return t2-t1
    

s=Solution()

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
#              8 is the missing number in the range since it does not appear in nums.
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))


# Input: nums = [3,0,1]
# Output: 2
print(s.missingNumber([3,0,1]))

# Input: nums = [0,1]
# Output: 2
print(s.missingNumber([0,1]))
