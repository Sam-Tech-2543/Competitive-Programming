# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/

class Solution1:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=""
        while columnNumber>0:
            ans+=chr(ord('A')+((columnNumber-1)%26))
            columnNumber=(columnNumber-1)//26

        return ans[::-1]
    

s=Solution1()

# Input: columnNumber = 701
# Output: "ZY"
s.convertToTitle(701)



# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution2:
    def titleToNumber(self, columnTitle: str) -> int:
        alphas="1ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=0
        power=0
        for i in columnTitle[::-1]:
            ans+=((alphas.index(i))*(26**power))
            power+=1

        return ans
    

s=Solution2()

# Input: columnTitle = "ZY"
# Output: 701
s.titleToNumber("ZY")