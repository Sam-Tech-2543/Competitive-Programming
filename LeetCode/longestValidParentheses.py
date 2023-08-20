# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                l = stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans
