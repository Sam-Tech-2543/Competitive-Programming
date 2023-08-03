# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    # Less Time Complexity
    def reverseVowels1(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s1 = [i for i in s]
        l1, l2 = [], []

        for n, i in enumerate(s1):
            if i in vowels:
                l1.append(i)
                l2.append(n)

        p = 0
        for i in l2[::-1]:
            s1[i] = l1[p]
            p += 1

        return "".join(s1)
    

    # Less Space Complexity
    def reverseVowels2(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l, r = 0, len(s) - 1

        s1 = list(s)

        while l < r:
            if s1[l] not in vowels:
                l+=1
            if s1[r] not in vowels:
                r-=1

            if s1[l] in vowels and s1[r] in vowels:
                s1[l], s1[r] = s1[r], s1[l]
                l+=1
                r-=1
            

        return "".join(s1)


s = Solution()

# Input: s = "hello"
# Output: "holle"
print(s.reverseVowels1("hello"))

# Input: s = "leetcode"
# Output: "leotcede"
print(s.reverseVowels2("leetcode"))
