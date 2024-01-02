# 2844. Minimum Operations to Make a Special Number
# https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution:
    def minimumOperations(self, num: str) -> int:
        last=[['0','0'],['2','5'],['5','0'],['7','5']]
        ans=float('inf')
        for i in last:
            curr=0
            j=1
            flag=1
            for k in range(len(num)-1,-1,-1):
                if num[k]!=i[j]:
                    curr+=1
                elif num[k]==i[j] and j==0:
                    flag=0
                    break
                elif num[k]==i[j]:
                    j=0

            if flag:
                nn=num.count('0')
                ans=min(ans,len(num)-nn)
            else:
                ans=min(ans,curr)

        return ans
    

s=Solution()

print(s.minimumOperations("2245047"))
print(s.minimumOperations("2908305"))
print(s.minimumOperations("10"))
