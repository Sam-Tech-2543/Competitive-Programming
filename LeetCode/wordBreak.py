# 139. Word Break
# https://leetcode.com/problems/word-break/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lst = [False] * (len(s) + 1)
        lst[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for j in wordDict:
                if i + len(j) <= len(s) and j == s[i : i + len(j)]:
                    lst[i] = lst[i + len(j)]
                if lst[i]:
                    break

        return lst[0]


s = Solution()


# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
print(s.wordBreak("leetcode", ["leet", "code"]))

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
print(s.wordBreak("applepenapple", ["apple", "pen"]))

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

# Input: s = "cars", wordDict = ["car","ca","rs"]
# Output: true
print(s.wordBreak("cars", ["car", "ca", "rs"]))
