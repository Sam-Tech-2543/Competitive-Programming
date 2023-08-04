# 1299. Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # l=0
        # while l<len(arr)-1:
        #     maxVal=max(arr[l+1:])
        #     arr[l]=maxVal
        #     l+=1
        # arr[-1]=-1

        # return arr
        lst=[-1]
        maxVal=-1
        for i in range(len(arr)-1,0,-1):
            maxVal=max(maxVal,arr[i])
            lst.append(maxVal)
        
        return lst[::-1]
        

s=Solution()

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
print(s.replaceElements([17,18,5,4,6,1]))