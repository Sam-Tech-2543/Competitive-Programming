# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = float("-inf")

        ans = 0
        for i in nums:
            ans += i
            if ans > maxVal:
                maxVal = ans

            if ans < 0:
                ans = 0

        return maxVal


s = Solution()

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
s.maxSubArray([1])

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
s.maxSubArray([5, 4, -1, 7, 8])
