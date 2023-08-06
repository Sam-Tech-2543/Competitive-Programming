# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Brute Force

        # minVal = float("inf")
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             sumVal = nums[i] + nums[j] + nums[k]
        #             if abs(sumVal - target) < abs(minVal):
        #                 minVal = sumVal - target

        # return target + minVal

        nums.sort()

        minVal = float("inf")
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(minVal - target):
                    minVal = s

                if s > target:
                    r -= 1
                else:
                    l += 1

        return minVal


s = Solution()


# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
print(s.threeSumClosest([-1, 2, 1, -4], 1))


# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
print(s.threeSumClosest([0, 0, 0], 1))
