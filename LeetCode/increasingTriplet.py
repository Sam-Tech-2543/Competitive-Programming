# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # myHash={}
        # for i in range(len(nums)-1,-1,-1):
        #     maxVal=0
        #     for j in myHash.keys():
        #         if nums[i]<nums[j]:
        #             maxVal=max(maxVal,myHash[j])

        #     myHash[i]=maxVal+1

        #     if myHash[i]>3:
        #         return True

        # return False

        n1, n2 = float("inf"), float("inf")
        for i in nums:
            if i <= n1:
                n1 = i
            elif i <= n2:
                n2 = i
            else:
                return True
        return False


s = Solution()

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
print(s.increasingTriplet([1, 2, 3, 4, 5]))

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
print(s.increasingTriplet([5, 4, 3, 2, 1]))
