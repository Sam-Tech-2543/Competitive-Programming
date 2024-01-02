from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        s=Counter(nums)

        lst=[]
        for i in s.items():
            lst.append(i)

        while lst:
            temp=[]
            removeIndex=[]
            for i in range(len(lst)):
                if lst[i][1]>0:
                    temp.append(lst[i][0])
                    lst[i]=(lst[i][0],lst[i][1]-1)
                else:
                    removeIndex.append(i)
            
            for i in removeIndex[::-1]:
                lst.pop(i)
            ans.append(temp)

        return ans[:-1]
    

s=Solution()

# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
nums = [1,3,4,1,2,3,1]
print(s.findMatrix(nums))

# Input: nums = [1,2,3,4]
# Output: [[4,3,2,1]]
nums = [1,2,3,4]
print(s.findMatrix(nums))