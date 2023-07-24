# 885. Spiral Matrix III
# https://leetcode.com/problems/spiral-matrix-iii/

from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        tot=rows*cols
        i,j=rStart,cStart
        n=0

        ans=[]

        c=0
        d="->"
        l=1

        while c<tot:
            if -1<i<rows and -1<j<cols:
                # print(i,j,d,l,n)
                ans.append([i,j])
                c+=1

            # print(i,j,d,l,n)

            if d=="->" and n<l:
                j+=1
                n+=1
                if n==l:
                    d="v"
                    n=0
            
            elif d=="v" and n<l:
                i+=1
                n+=1
                if n==l:
                    d="<-"
                    l+=1
                    n=0

            elif d=="<-" and n<l:
                j-=1
                n+=1
                if n==l:
                    d="^"
                    n=0

            elif d=="^" and n<l:
                i-=1
                n+=1
                if n==l:
                    d="->"
                    n=0
                    l+=1

        # print(ans)

        return ans
    

s=Solution()


# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [ [1,4],[1,5],[2,5],[2,4],[2,3],[1,3],
#           [0,3],[0,4],[0,5],[3,5],[3,4],[3,3],
#           [3,2],[2,2],[1,2],[0,2],[4,5],[4,4],
#           [4,3],[4,2],[4,1],[3,1],[2,1],[1,1],
#           [0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

print(s.spiralMatrixIII(5,6,1,4))

# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]

print(s.spiralMatrixIII(1,4,0,0))