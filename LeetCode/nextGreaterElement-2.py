# 503. Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*(len(nums))

        for i in range(len(nums)):
            # lst1=[j for j in range(i,len(nums))]
            # lst2=[j for j in range(0,i)]
            # print(lst1,lst2)
            flag=True
            for j in range(i,len(nums)):
                if nums[i]<nums[j]:
                    ans[i]=nums[j]
                    flag=False
                    break

            if flag:
                for j in range(0,i):
                    if nums[i]<nums[j]:
                        ans[i]=nums[j]
                        break

        return ans
    

s=Solution()

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
# print(s.nextGreaterElements([1,2,3,4,3]))
s.nextGreaterElements([1,2,3,4,3])