# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List
import heapq


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        s = int(s / 2)

        dp = [False] * (s + 1)
        dp[0] = True

        for num in nums:
            for j in range(s, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[s]


s = Solution()
print(s.canPartition([1, 5, 11, 5]))


# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         self.s=sum(nums)
#         if self.s%2!=0:
#             return False

#         self.s/=2

#         dp={}

#         def recursion(i,currVal):
#             if currVal==self.s:
#                 return True
#             if i>=len(nums):
#                 return False

#             tup=(i, currVal)
#             if tup in dp:
#                 return dp[tup]

#             dp[(i,currVal)] = recursion(i+1,currVal+nums[i]) or recursion(i+1,currVal)

#             return dp[(i,currVal)]

#         return recursion(0,0)
