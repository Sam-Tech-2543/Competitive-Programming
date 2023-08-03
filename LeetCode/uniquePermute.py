# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/

from typing import List

class Solution:
    def permuteUniqueLong(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        if len(nums)==1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n=nums.pop(0)

            lst=self.permuteUnique(nums)
            for i in lst:
                i.append(n)

            ans.extend(lst)

            for j in lst:
                if j not in ans:
                    ans.append(j)

            nums.append(n)

        return ans
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        lst=[]
        countDict={}

        for i in nums:
            if i not in countDict:
                countDict[i]=1
            else:
                countDict[i]+=1

        def dfs():
            if len(lst)==len(nums):
                ans.append(lst.copy())
                return
            
            for i in countDict:
                if countDict[i]>0:
                    lst.append(i)
                    countDict[i]-=1

                    dfs()

                    countDict[i]+=1
                    lst.pop()

        dfs()

        return ans
    

s=Solution()

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

s.permuteUnique([1,1,2])