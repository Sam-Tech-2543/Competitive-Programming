# 1218. Longest Arithmetic Subsequence of Given Difference
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

from typing import List

class Solution:
    def find(self,arr,key):
        ans=-1
        for i in range(len(arr)):
            if key==arr[i]:
                ans=i
        return ans

    def longestSubsequenceTLE(self, arr: List[int], difference: int) -> int:
        lst=[0]*len(arr)
        ans=0
        
        for i in range(len(arr)):
            temp=self.find(arr[:i],arr[i]-difference)
            if temp!=-1:
                lst[i]=1+lst[temp]
            else:
                lst[i]=1

            ans=max(lst[i],ans)

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lst={}
        ans=0

        for i in arr:
            lst[i]=lst.get(i-difference,0)+1
            ans=max(ans,lst[i])

            print(lst)

        return ans
    

s=Solution()

print(s.longestSubsequence([29,1,2,378,3,4,5,6,10,20],1))

# Input: arr = [1,2,3,4], difference = 1
# Output: 4
print(s.longestSubsequence([1,2,3,4],1))

# Input: arr = [1,3,5,7], difference = 1
# Output: 1
print(s.longestSubsequence([1,3,5,7],1))

# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
s.longestSubsequence([1,5,7,8,5,3,4,2,1],-2)
