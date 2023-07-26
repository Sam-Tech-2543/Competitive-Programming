# 198. House Robber
# https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        ans=max(nums[:2])
        for i in range(2,len(nums)):
            maxV=max(nums[:i-1])
            nums[i]=nums[i]+maxV
            ans=max(ans,nums[i])

        return ans
    

s=Solution()


# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
print(s.rob([1,2,3,1]))


# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
print(s.rob([2,7,9,3,1]))

print(s.rob([1]))
