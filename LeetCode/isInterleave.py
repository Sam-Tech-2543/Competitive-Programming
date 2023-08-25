class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.cache = {}

        if len(s1) + len(s2) != len(s3):
            return False

        def recursion(i1, i2, i3):
            status = False

            while i3 < len(s3):
                if (i1, i2, i3) in self.cache:
                    return self.cache[(i1, i2, i3)]

                if i1 < len(s1) and i2 < len(s2) and s1[i1] == s2[i2] == s3[i3]:
                    status = recursion(i1 + 1, i2, i3 + 1) or status
                    if status:
                        return True
                    else:
                        self.cache[(i1 + 1, i2, i3 + 1)] = False

                    status = recursion(i1, i2 + 1, i3 + 1) or status
                    if status:
                        return True
                    else:
                        self.cache[(i1, i2 + 1, i3 + 1)] = False

                if i1 < len(s1) and s1[i1] == s3[i3]:
                    i1 += 1
                    i3 += 1
                elif i2 < len(s2) and s2[i2] == s3[i3]:
                    i2 += 1
                    i3 += 1
                else:
                    return status

            if i3 == len(s3):
                return True

        return recursion(0, 0, 0)


s = Solution()

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(s.isInterleave(s1, s2, s3))


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(s.isInterleave(s1, s2, s3))

s1 = ""
s2 = ""
s3 = "a"
print(s.isInterleave(s1, s2, s3))

s1 = "aa"
s2 = "ab"
s3 = "aaba"
print(s.isInterleave(s1, s2, s3))

s1 = "ab"
s2 = "bc"
s3 = "babc"
print(s.isInterleave(s1, s2, s3))

s1 = "a"
s2 = ""
s3 = "a"
print(s.isInterleave(s1, s2, s3))

s1 = "aabaac"
s2 = "aadaaeaaf"
s3 = "aadaaeaabaafaac"
print(s.isInterleave(s1, s2, s3))


s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
print(s.isInterleave(s1, s2, s3))

s1 = "cacbbbaaabbacbbbbabbcaccccabaaacacbcaacababbaabbaccacbaabac"
s2 = "cbcccabbbbaaacbaccbabaabbccbbbabacbaacccbbcaabaabbbcbcbab"
s3 = "ccbcccacbabbbbbbaaaaabbaaccbabbbbacbcbcbaacccbacabbaccbaaabcacbbcabaabacbbcaacaccbbacaabababaabbbaccbbcacbbacabbaacb"
print(s.isInterleave(s1, s2, s3))


# class Solution:
#     def check(self, s1, s2, s3, i1, i2, i3):
#         if (i1, i2, i3) in self.cache:
#             return self.cache[(i1, i2, i3)]

#         status=False

#         while i3<len(s3):
#             if i1<len(s1) and i2<len(s2) and s1[i1]==s2[i2]==s3[i3]:
#                 status=self.check(s1, s2, s3, i1+1, i2, i3+1) or status
#                 if status:
#                     return True
#                 else:
#                     self.cache[(i1+1, i2, i3+1)]=False

#                 status=self.check(s1, s2, s3, i1, i2+1, i3+1) or status
#                 if status:
#                     return True
#                 else:
#                     self.cache[(i1, i2+1, i3+1)]=False

#             if i1<len(s1) and s1[i1]==s3[i3]:
#                 i1+=1
#                 i3+=1
#             elif i2<len(s2) and s2[i2]==s3[i3]:
#                 i2+=1
#                 i3+=1
#             else:
#                 return status

#         if i3==len(s3):
#             return True

#         return status


#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         self.cache={}

#         if len(s1)+len(s2)!=len(s3):
#             return False

#         i1, i2, i3=0, 0, 0
#         status=False

#         while i3<len(s3):
#             if i1<len(s1) and i2<len(s2) and s1[i1]==s2[i2]==s3[i3]:
#                 status=self.check(s1, s2, s3, i1+1, i2, i3+1) or status
#                 if status:
#                     return True
#                 else:
#                     self.cache[(i1+1, i2, i3+1)]=False

#                 status=self.check(s1, s2, s3, i1, i2+1, i3+1) or status
#                 if status:
#                     return True
#                 else:
#                     self.cache[(i1, i2+1, i3+1)]=False

#             if i1<len(s1) and s1[i1]==s3[i3]:
#                 i1+=1
#                 i3+=1
#             elif i2<len(s2) and s2[i2]==s3[i3]:
#                 i2+=1
#                 i3+=1
#             else:
#                 return status

#         if i3==len(s3):
#             return True

#         return status
