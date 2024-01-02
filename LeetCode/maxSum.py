from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans=0
        l,r=0,k
        lst=nums[l:r]   
        s=sum(lst)

        if len(set(lst))>=m:
            ans=max(s,ans)

        while r<len(nums):
            n=lst.pop(0)
            s-=n
            lst.append(nums[r])
            s+=nums[r]

            if len(set(lst))>=m:
                ans=max(s,ans)

            l+=1
            r+=1
        
        return ans

s=Solution()

# Input: nums = [2,6,7,3,1,7], m = 3, k = 4
# Output: 18
print(s.maxSum([2,6,7,3,1,7],3,4))

# Input: nums = [5,9,9,2,4,5,4], m = 1, k = 3
# Output: 23
print(s.maxSum([5,9,9,2,4,5,4],1,3))

# Input: nums = [1,2,1,2,1,2,1], m = 3, k = 3
# Output: 0
print(s.maxSum([1,2,1,2,1,2,1],3,3))

# [1,1,2,2] 1 3
print(s.maxSum([1,1,2,2],1,3))

print(s.maxSum([1,1,1,3],2,2))



# def maxSum(self, nums: List[int], m: int, k: int) -> int:
#     ans=0

#     for i in range(len(nums)-k+1):
#         mySet=set()
#         c=0
#         s=0
#         for j in range(i,i+k):
#             if nums[j] not in mySet:
#                 mySet.add(nums[j])
#                 c+=1
#             s+=nums[j]
#         if c>=m:
#             ans=max(ans,s)

#     return ans