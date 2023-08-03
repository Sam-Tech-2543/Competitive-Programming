# 443. String Compression
# https://leetcode.com/problems/string-compression/

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # ans=[]
        # myHash={i:0 for i in chars}

        # for i in chars:
        #     myHash[i]+=1

        # for i in myHash.keys():
        #     if myHash[i]==1:
        #         ans+=i
        #     else:
        #         ans+=i
        #         ans+=str(myHash[i])

        # return ans

        l, r = 0, 0
        s = len(chars)

        while l < s:
            n = 0
            r = l
            while r < s and chars[l] == chars[r]:
                if chars[l] == chars[r]:
                    n += 1
                r += 1

            if n > 1:
                for k in range(l + 1, r):
                    chars.pop(l + 1)
                    s -= 1
                for k in range(len(str(n))):
                    l = l + 1
                    chars.insert(l, str(n)[k])
                    s += 1

            l += 1
            r = l

        return len(chars)


s = Solution()

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))


# # Input: chars = ["a"]
# # Output: Return 1, and the first character of the input array should be: ["a"]
# # Explanation: The only group is "a", which remains uncompressed since it's a single character.
# print(s.compress(["a"]))


print(s.compress(["a", "a", "a", "b", "b", "a", "a"]))
