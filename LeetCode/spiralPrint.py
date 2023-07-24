# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a=matrix
        n1=len(a)
        n2=len(a[0])
        
        if(n2==1):
            return [i[0] for i in matrix]

        i1=0
        i2=0

        d="->" # Direction
        l=0 #Loop Number

        lst=[] #Output List

        #Looping the input for each element
        for i in range(n2*n1):
            lst.append(a[i1][i2]) #Adding the Number to the Output List

            if i2<n2-1-l and d=="->": #Right Direction
                i2+=1
                if i2==n2-1-l:
                    d="v"
            elif i1<n1-1-l and d=="v": #Down Direction
                i1+=1
                if i1==n1-1-l:
                    d="<-"
            elif i2>0+l and d=="<-": #Left Direction
                i2-=1
                if i2==0+l:
                    d="^"
            elif i1>0+l and d=="^": #Up Direction
                i1-=1
                if i1==1+l:
                    d="->"
                    l+=1

        return lst
    

s=Solution()

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))