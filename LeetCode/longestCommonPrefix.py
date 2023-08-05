# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        # Checking the Common Prefix for first two strings
        prefix = ""
        for i in range(len(strs[0])):
            if i < len(strs[1]) and strs[0][i] == strs[1][i]:
                prefix += strs[0][i]
            else:
                break

        # Checking the Common Prefix for remaining strings
        for i in range(2, len(strs)):
            ans = ""
            for j in range(len(strs[i])):
                if j < len(prefix) and strs[i][j] == prefix[j]:
                    ans += prefix[j]
                else:
                    break
            prefix = ans

        return prefix


s = Solution()

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
s.longestCommonPrefix(["flower", "flow", "flight"])

# Input: strs = ["dog","racecar","car"]
# Output: ""
s.longestCommonPrefix(["dog", "racecar", "car"])
