# 1995. Count Special Quadruplets
# https://leetcode.com/problems/count-special-quadruplets/

from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # if len(nums)<4:
        #     return 0
        
        # nums.sort()

        # ans=0
        # l,m,r=0,1,2
        # while r<len(nums)-1:
        #     n=nums[l]+nums[m]+nums[r]
        #     if n==nums[r+1]:
        #         ans+=1
        #         r+=1
        #     else:
        #         l+=1
        #         m+=1
        #         r+=1

        # print(ans)

        # return ans

        if len(nums)<4:
            return 0
        

        ans=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if nums[i]+nums[j]+nums[k]==nums[l]:
                            ans+=1
    
        print(ans)

        return ans

s=Solution()

# Input: nums = [3,3,6,4,5]
# Output: 0
# Explanation: There are no such quadruplets in [3,3,6,4,5].
s.countQuadruplets([3,3,6,4,5])

# Input: nums = [1,2,3,6]
# Output: 1
# Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
s.countQuadruplets([1,2,3,6])

# Input: nums = [1,1,1,3,5]
# Output: 4
# Explanation: The 4 quadruplets that satisfy the requirement are:
# - (0, 1, 2, 3): 1 + 1 + 1 == 3
# - (0, 1, 3, 4): 1 + 1 + 3 == 5
# - (0, 2, 3, 4): 1 + 1 + 3 == 5
# - (1, 2, 3, 4): 1 + 1 + 3 == 5
s.countQuadruplets([1,1,1,3,5])