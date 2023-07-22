# 6930. Check if Array is Good
# https://leetcode.com/contest/biweekly-contest-109/problems/check-if-array-is-good/

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        s1,s2=0,0
        for i in range(len(nums)):
            s1+=nums[i]
            s2+=(i+1)

        return s2-1==s1


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