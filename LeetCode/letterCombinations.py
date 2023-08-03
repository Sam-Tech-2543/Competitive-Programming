# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myHash = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) >= 1:
            alphas = myHash[digits[0]]
            lst = [i for i in alphas]
        else:
            return []

        for i in range(1, len(digits)):
            alphas = myHash[digits[i]]
            tlst = []
            while lst != []:
                t = lst.pop()
                for k in alphas:
                    tlst.append(t + k)
            lst = tlst

        return lst


s = Solution()


# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
s.letterCombinations("23")

# Input: digits = "2"
# Output: ["a","b","c"]
s.letterCombinations("2")
