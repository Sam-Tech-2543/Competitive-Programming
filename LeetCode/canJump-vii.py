from collections import deque

class Solution:
    def canReach_TLE(self, s: str, minJump: int, maxJump: int) -> bool:

        dp={}

        def recursion(curr):
            if curr in dp:
                return dp[curr]

            if curr==len(s)-1:
                return True
            elif curr>=len(s):
                dp[curr]=False
                return False
            
            for i in range(minJump,maxJump+1):
                n=curr+i
                if n<len(s) and s[n]=='0':
                    ans = recursion(n)
                    dp[n]=ans
                    if ans:
                        return True
                    
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q=deque([0])
        far=0

        while q:
            i=q.popleft()
            start=max(i+minJump, far+1)
            for j in range(start, min(i+maxJump+1, len(s))):
                if s[j]=="0":
                    q.append(j)
                    if j==len(s)-1:
                        return True
            far=i+maxJump

        return False

        return recursion(0)