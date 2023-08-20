# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

import math
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # For Rows
        for i in board:
            r=set()
            for j in i:
                if j.isnumeric():
                    if j in r:
                        return False
                    r.add(j)

        # For Columns
        for i in range(9):
            c=set()
            for j in range(9):
                t=board[j][i]
                if t.isnumeric():
                    if t in c:
                        return False
                    c.add(t)

        # For 3*3 Grid
        myHash={}
        for i in range(3):
            for j in range(3):
                myHash[(i,j)]=set()

        for r in range(9):
            for c in range(9):
                nr=math.floor(r/3)
                nc=math.floor(c/3)

                t=board[r][c] 
                if t.isnumeric():
                    if t in myHash[(nr,nc)]:
                        return False
                    else:
                        myHash[(nr,nc)].add(t)


        return True

