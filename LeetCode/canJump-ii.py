# 45. Jump Game
# https://leetcode.com/problems/jump-game-ii/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # ans = 0

        # lst = []

        # goal = len(nums) - 1
        # for i in range(len(nums) - 2, -1, -1):
        #     if nums[i] >= (goal - i):
        #         n = i + nums[i]
        #         print(f"{n=}")

        #         j = 0
        #         while j < len(lst):
        #             if lst[j] < n:
        #                 lst.pop(j)
        #                 ans-=1
        #             j += 1
        #             print("While:",lst)

        #         goal = i
        #         lst.append(i)
        #         ans+=1

        #     print(lst)

        # print(lst, nums)

        # return ans

        ans = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            far = 0
            for i in range(l, r + 1):
                far = max(far, nums[i] + i)
            l = r + 1
            r = far
            ans += 1

        return ans


s = Solution()

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.
print(s.jump([2, 3, 1, 1, 4]))


# Input: nums = [2,3,0,1,4]
# Output: 2
print(s.jump([2, 3, 0, 1, 4]))
