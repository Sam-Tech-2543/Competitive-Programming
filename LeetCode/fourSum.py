# 18. 4Sum
# https://leetcode.com/problems/4sum/

from typing import List


class Solution:
    def fourSumBruteForce(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    lst = [nums[i], nums[j], nums[l], nums[r]]
                    if s == target:
                        ans.append(lst)
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1

        return ans

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans, temp = [], []

        def helper(toFind, s, target):
            if toFind != 2:
                for i in range(s, len(nums) - toFind + 1):
                    if i > s and nums[i] == nums[i - 1]:
                        continue
                    temp.append(nums[i])
                    helper(toFind - 1, i + 1, target - nums[i])
                    temp.pop()
                return

            l = s
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    ans.append(temp.copy() + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        helper(4, 0, target)

        return ans


s = Solution()

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# s.fourSum([1,0,-1,0,-2,2],0)

# Input: nums = [-3,-2,-1,0,0,1,2,3] target=0
# Output: [ [-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],
#           [-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
