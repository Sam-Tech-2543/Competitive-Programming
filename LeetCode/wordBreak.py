# 139. Word Break
# https://leetcode.com/problems/word-break/

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lst=[False]*(len(s)+1)
        lst[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for j in wordDict:
                if i+len(j)<=len(s) and j==s[i:i+len(j)]:
                    lst[i]=lst[i+len(j)]
                if lst[i]:
                    break

        return lst[0]

