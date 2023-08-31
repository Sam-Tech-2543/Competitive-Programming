from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans=[]

        def dfs(i,lst):
            if i==len(s):
                self.ans.append(' '.join(lst))
                return

            for j in range(i,len(s)):
                w=s[i:j+1]
                if w in wordDict:
                    lst.append(w)
                    dfs(j+1,lst)
                    lst.pop()
            
        dfs(0,[])

        return self.ans