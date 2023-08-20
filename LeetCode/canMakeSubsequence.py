# 2825. Make String a Subsequence Using Cyclic Increments
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        alphas = "abcdefghijklmnopqrstuvwxyza"
        j = 0
        n2 = len(str2)
        for i in range(len(str1)):
            if j >= n2:
                return True
            if str1[i] == str2[j] or str2[j] == alphas[alphas.index(str1[i]) + 1]:
                j += 1

        return j >= n2


s = Solution()
# print(s.canMakeSubsequence("zc","ad"))
print(s.canMakeSubsequence("dm", "e"))
