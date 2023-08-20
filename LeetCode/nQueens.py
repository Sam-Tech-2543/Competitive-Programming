# 51. N-Queens
# https://leetcode.com/problems/n-queens/

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols,pd,nd=set(),set(),set()
        # pd -> r+c, nd -> r-c 

        ans=[]
        board=[["."]*n for r in range(n)]

        def backTracking(r):
            if r==n:
                temp=["".join(row) for row in board]
                ans.append(temp)
                return

            for c in range(n):
                if c in cols or r+c in pd or r-c in nd:
                    continue
                
                cols.add(c)
                pd.add(r+c)
                nd.add(r-c)
                board[r][c]="Q"

                backTracking(r+1)

                cols.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
                board[r][c]="."


        backTracking(0)

        return ans
