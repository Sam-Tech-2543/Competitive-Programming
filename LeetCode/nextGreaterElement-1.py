# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

from typing import List

class Solution:
    def nextGreaterElement_nSquare(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*(len(nums1))

        for i in range(len(nums1)):
            k=nums2.index(nums1[i])
            for j in range(k,len(nums2)):
                if nums2[j]>nums1[i]:
                    ans[i]=nums2[j]
                    break

        return ans
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myHash={}
        for i in nums1:
            myHash[i]=-1

        stack=[nums2[0]]

        for i in range(1,len(nums2)):
            t=stack[-1]
            if nums2[i]<t:
                stack.append(nums2[i])
            else:
                while nums2[i]>t and stack!=[]:
                    temp=myHash.get(t,False)
                    if temp:
                        myHash[t]=nums2[i]
                    t=stack.pop()
                    if t>nums2[i]:
                        stack.append(t)

                if t<nums2[i]:
                    temp=myHash.get(t,False)
                    if temp:
                        myHash[t]=nums2[i]
                stack.append(nums2[i])
        
        return list(myHash.values())
    

s=Solution()

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# print(s.nextGreaterElement([4,1,2], [1,3,4,2]))


# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
# print(s.nextGreaterElement([2,4], [1,2,3,4]))

# nums1 = [4,1,2]
# nums2 = [1,2,3,4]
# [-1,2,3]
# print(s.nextGreaterElement([4,1,2], [1,2,3,4]))

# nums1 = [1,3,5,2,4]
# nums2 = [5,4,3,2,1]
# [-1,-1,-1,-1,-1]
# print(s.nextGreaterElement([1,3,5,2,4], [5,4,3,2,1]))

# nums1 = [1,3,5,2,4,6,7]
# nums2 = [6,5,4,3,2,1,7]
# [7,7,7,7,7,7,-1]
# print(s.nextGreaterElement([1,3,5,2,4,6,7], [6,5,4,3,2,1,7]))

print(s.nextGreaterElement([137], [137,59,92,122,52,131,79,236]))
