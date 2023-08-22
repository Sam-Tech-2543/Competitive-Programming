# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0 or len(nums)==0 or len(nums)==1:
            return False

        target=int(s/2)

        mySet=set()
        mySet.add(0)

        for i in range(len(nums)-1,-1,-1):
            newSet=set()
            for j in mySet:
                s=j+nums[i]
                if s==target:
                    return True
                newSet.add(s)
                newSet.add(j)

            mySet=newSet

        return False



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
