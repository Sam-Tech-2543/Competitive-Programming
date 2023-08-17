# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

from typing import List

class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if k==1:
    #         return nums

    #     l=0
    #     maxVal=max(nums[l:l+k])
    #     s=sum(nums[l:l+k])
    #     ans=[maxVal]

    #     l+=1

    #     while (l+k)<=len(nums):
    #         if maxVal==nums[l-1]:
    #             maxVal=max(nums[l:l+k])
    #         else:
    #             maxVal=max(maxVal,nums[l+k-1])

    #         l+=1
    #         ans.append(maxVal)

    #     return ans
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums

        lst=[]

        r=0
        while r<k:
            while lst and nums[r]>nums[lst[-1]]:
                lst.pop()    
            lst.append(r)
            r+=1

        ans=[nums[lst[0]]]
        print(lst)

        l=1        
        while r<len(nums):
            while lst and nums[r]>nums[lst[-1]]:
                lst.pop()
            lst.append(r)

            if l>lst[0]:
                lst.pop(0)

            ans.append(nums[lst[0]])

            r+=1
            l+=1
            print(lst)
        return ans


s=Solution()
s.maxSlidingWindow([10,9,8,7,11,5,4,3,2,1],4)