# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p, i = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[p]:
                p += 1
                if p == len(needle):
                    return i - p + 1
            else:
                i -= p
                p = 0
            i += 1

        return -1


s = Solution()

haystack = "mississippi"
needle = "issip"
print(s.strStr(haystack, needle))
