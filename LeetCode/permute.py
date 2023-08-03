# 46. Permutations
# https://leetcode.com/problems/permutations/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        if len(nums)==1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n=nums.pop(0)

            lst=self.permute(nums)
            for i in lst:
                i.append(n)

            ans.extend(lst)

            nums.append(n)

        return ans

s=Solution()

print(s.permute([1,2,3]))