# What Mean do you Mean?
# https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-112/problems


from typing import List


class Solution:
    def IsMean(self, n : int, k : int, x : int, arr : List[int]) -> bool:
        arr.sort()
        a=sum(arr)
        
        l,r=0,n-1
        while l<r:
            temp=a
            
            n1=arr[l]
            a-=n1
            a+=n1*k
            
            n2=arr[r]
            a-=n2
            a+=n2*k
            
            ans=a/n
            
            if ans==x:
                return True
            elif ans>x:
                a=temp
                r-=1
            elif ans<x:
                a=temp
                l+=1
            
        return False
    

s=Solution()


# Input :
# n = 3
# k = 5
# arr = [1, 2, 3]
# x = 6
# Output: 
# true
# Explanation: 
# You can multiply k = 5 to the first and second indices, the resulting array becomes [5, 10, 3] whose mean is x = 6.
print(s.IsMean(3,5,6,[1,2,3]))