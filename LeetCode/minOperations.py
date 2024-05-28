from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s=Counter(nums)
        print(s)
        ans=0
        for i in s.values():
            if i%3==0:
                ans+=(i/3)
            elif i%3==2:
                ans+=((i-2)/3)
                ans+=1
            elif i%3==1 and i>4:
                ans+=((i-4)/3)
                ans+=2
            elif i%2==0:
                ans+=(i/2)
            else:
                return -1
                     
        return int(ans)
    

s=Solution()

# Input: nums = [2,3,3,2,2,4,2,3,4]
# Output: 4
nums = [2,3,3,2,2,4,2,3,4]
print(s.minOperations(nums))

# Input: nums = [2,1,2,2,3,3]
# Output: -1
nums = [2,1,2,2,3,3]
print(s.minOperations(nums))