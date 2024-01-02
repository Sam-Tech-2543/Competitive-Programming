class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return sorted(s1[0::2])==sorted(s2[0::2]) and sorted(s1[1::2])==sorted(s2[1::2])
    
s=Solution()

# Input: s1 = "abcdba", s2 = "cabdab"
# Output: true
# Explanation: We can apply the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
# - Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
# - Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
print(s.checkStrings("abcdba", "cabdab"))