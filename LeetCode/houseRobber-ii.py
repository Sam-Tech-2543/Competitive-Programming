# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/

from typing import List

class Solution:
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans=max(nums[:2])
        for i in range(2,len(nums)):
            maxV=max(nums[:i-1])
            nums[i]=max(nums[i],nums[i]+maxV)
            ans=max(nums[i],ans)

        return ans

    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
    

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
