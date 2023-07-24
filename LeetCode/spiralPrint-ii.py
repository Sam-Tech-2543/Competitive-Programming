# 59. Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for i in range(n)] for i in range(n)]
        tot=n**2

        i,j=0,0
        n1,n2=n,n
        c=0

        d="->"
        l=0

        while c<tot:
            c+=1
            # print(i,j,d)
            ans[i][j]=c

            if d=="->" and j<n2-l-1:
                j+=1
                if j==n2-l-1:
                    d="v"
            elif d=="v" and i<n1-l-1:
                i+=1
                if i==n2-l-1:
                    d="<-"
            elif d=="<-" and j>l:
                j-=1
                if j==l:
                    d="^"
            elif d=="^" and i>l:
                i-=1
                if i==l+1:
                    d="->"
                    l+=1

        return ans

s=Solution()

# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
n = 3
print(s.generateMatrix(n))

# Input: n = 1
# Output: [[1]]
print(s.generateMatrix(1))