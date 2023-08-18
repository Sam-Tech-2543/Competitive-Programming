# 67. Add Binary
# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0" and b=="0":
            return "0"

        a = int(a, 2)
        b = int(b, 2)

        mainAns = str()

        ans = 0
        c = 0

        while a != 0 and b != 0:
            a1 = a & 1
            b1 = b & 1

            if a1 and b1 and c:
                ans = 1
                c = 1
            elif (a1 and b1) or (c and (a1 or b1)):
                ans = 0
                c = 1
            elif (a1 or b1) or (not a1 and not b1 and c) or c:
                ans = 1
                c = 0
            else:
                ans = 0
                c = 0

            mainAns += str(ans)

            a >>= 1
            b >>= 1

        temp = a if a else b
        while temp:
            t = temp & 1
            if t and c:
                ans = 0
                c = 1
            elif t or c:
                ans = 1
                c = 0
            else:
                ans = 0
                c = 0

            mainAns += str(ans)

            temp >>= 1

        if c:
            ans = c
            mainAns += str(ans)

        return mainAns[::-1]


s = Solution()


# # Input: a = "11", b = "1"
# # Output: "100"
# print(s.addBinary("11","1"))

# # Input: a = "1010", b = "1011"
# # Output: "10101"
# print(s.addBinary("1010","1011"))

# Input: a = "110010", b = "10111"
# Output: "1001001"
print(s.addBinary("110010", "10111"))

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a=int(a,2)
#         b=int(b,2)

#         mainAns=int("0",2)

#         ans=0
#         c=0

#         while a!=0 and b!=0:
#             a1=a&1
#             b1=b&1

#             if a1 and b1 and c:
#                 ans=1
#                 c=1
#             elif a1 and b1:
#                 ans=0
#                 c=1
#             elif a1 or b1 or (not a1 and not b1 and c):
#                 ans=1
#                 c=0
#             else:
#                 ans=0
#                 c=0

#             mainAns<<=1
#             mainAns|=ans
#             print(ans,mainAns)

#             a>>=1
#             b>>=1

#         temp= a if a else b
#         while temp:
#             t=temp&1
#             if t and c:
#                 ans=0
#                 c=1
#             elif t or c:
#                 ans=1
#                 c=0
#             else:
#                 ans=0
#                 c=0

#             mainAns<<=1
#             mainAns|=ans
#             print(ans, mainAns)

#             temp>>=1

#         if c:
#             ans=c
#             mainAns<<=1
#             mainAns|=ans
#             print(ans, mainAns)

#         print(bin(mainAns))
