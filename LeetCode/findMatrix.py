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
    # def findMatrix(self, nums: List[int]) -> List[List[int]]:
    #     ans=[]
    #     old=set()
    #     temp=[]

    #     for i in nums:
    #         if i not in old:
    #             old.add(i)
    #             temp.append(i)
    #         else:
    #             ans.append(temp)
    #             temp=[]
    #             flag=1
    #             for j in range(len(ans)):
    #                 if i not in ans[j]:
    #                     ans[j].append(i)
    #                     flag=0
    #                     break
    #             if flag:
    #                 temp.append(i)

    #     if temp:
    #         ans.append(temp)

    #     return ans    

s=Solution()

# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
nums = [1,3,4,1,2,3,1]
print(s.findMatrix(nums))

# Input: nums = [1,2,3,4]
# Output: [[4,3,2,1]]
nums = [1,2,3,4]
print(s.findMatrix(nums))