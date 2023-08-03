# 55. Jump Game
# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= (goal - i):
                goal = i

        return goal == 0


s = Solution()

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
print(s.canJump([2, 3, 1, 1, 4]))
