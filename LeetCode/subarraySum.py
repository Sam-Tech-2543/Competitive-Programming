# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        myHash={0:1} # Prefix Sum: Count

        s=0
        for i in nums:
            s+=i

            n=s-k
            g=myHash.get(n,None)
            if g:
                ans+=g
        
            g=myHash.get(s,None)
            if g:
                myHash[s]+=1
            else:
                myHash[s]=1

        return ans
    

s=Solution()
print(s.subarraySum([1,1,1],2))

print(s.subarraySum([1,2,3],3))