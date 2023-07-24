# 6930. Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # s1,s2=0,0
        # for i in range(len(nums)):
        #     s1+=nums[i]
        #     s2+=(i+1)

        # return s2-1==s1

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if  nums[i]!=i+1:
        #         return False
        #     if nums[i]==nums[i+1]:
        #         if i==len(nums)-2:
        #             return True
        #         else:
        #             return False

        # return False
            
        s1,s2=0,0
        maxVal=0
        for i in range(len(nums)):
            s1+=nums[i]
            s2+=(i+1)
            if maxVal<nums[i]:
                maxVal=nums[i]

        count=0
        for i in nums:
            if i==maxVal:
                count+=1

        return (count==2 and s1+1==s2)


s=Solution()

# Input: nums = [2, 1, 3]
# Output: false
nums = [2, 1, 3]
print(s.isGood(nums))

# Input: nums = [1, 3, 3, 2]
# Output: true
nums = [1, 3, 3, 2]
print(s.isGood(nums))

# Input: nums = [1, 1]
# Output: true
nums = [1, 1]
print(s.isGood(nums))

# Input: nums = [3, 4, 4, 1, 2, 1]
# Output: false
nums = [3, 4, 4, 1, 2, 1]
print(s.isGood(nums))