# 2369. Check if There is a Valid Partition For The Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        two = nums[-1] == nums[-2]
        if len(nums) == 2:
            return two

        three = (nums[-1] == nums[-2] == nums[-3]) or (
            nums[-3] + 1 == nums[-2] == nums[-1] - 1
        )

        dp = [three, two, False]
        for i in range(len(nums) - 4, -1, -1):
            curr = (nums[i] == nums[i + 1]) and dp[1]
            curr = (
                curr
                or (
                    (nums[i] == nums[i + 1] == nums[i + 2])
                    or (nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1)
                )
                and dp[2]
            )

            dp = [curr, dp[0], dp[1]]

        return dp[0]


s = Solution()

# Input: nums = [4,4,4,5,6]
# Output: true
# Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
# This partition is valid, so we return true.
print(s.validPartition([4, 4, 4, 5, 6]))
