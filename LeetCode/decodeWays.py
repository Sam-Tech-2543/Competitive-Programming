# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        self.ans=0
        dp={len(s):1}

        def dfs(i):
            if i in dp:
                self.ans+=dp[i]
                return dp[i]
            elif i>len(s)-1 or s[i]=="0":
                return 0
            
            temp=dfs(i+1)
            if i+1<len(s) and s[i]!=0 and int(s[i]+s[i+1])<=26:
                temp+=dfs(i+2)

            dp[i]=temp
            return temp

        dfs(0)

        return self.ans
