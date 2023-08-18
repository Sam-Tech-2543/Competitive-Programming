from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = digits[-1] + 1
        if s >= 10:
            digits[-1] = s % 10
            c = 1
        else:
            digits[-1] = s
            return digits

        i = len(digits) - 2
        while i >= 0 and c:
            s = digits[i] + c
            if s >= 10:
                digits[i] = s % 10
                c = 1
            else:
                digits[i] = s
                c = 0
            i -= 1

        if c:
            digits.insert(0, 1)

        return digits


s = Solution()
print(s.plusOne([1, 2, 3]))
