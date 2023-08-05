# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     s = set()
    #     for i in range(len(nums) - 1, -1, -1):
    #         n = nums[i]
    #         if n in s:
    #             nums.pop(i)
    #         else:
    #             s.add(n)

    #     return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[p] = nums[i]
                p += 1

        return p


s = Solution()

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
nums = [1, 1, 2]
print(s.removeDuplicates(nums), nums)

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums), nums)
