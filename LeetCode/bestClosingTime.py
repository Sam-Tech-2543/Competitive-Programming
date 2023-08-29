# 2483. Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix=[0]
        suffix=[0]*(len(customers)+1)

        # Prefix
        for i in range(1,len(customers)+1):
            if customers[i-1]=="N":
                prefix.append(prefix[i-1]+1)
            else:
                prefix.append(prefix[i-1])

        # Suffix
        for i in range(len(customers)-1,-1,-1):
            if customers[i]=="Y":
                suffix[i]=suffix[i+1]+1
            else:
                suffix[i]=suffix[i+1]

        # Find Minimum Hour to close the shop
        minVal=float('inf')
        minIndex=float('inf')
        for i in range(len(prefix)):
            s=prefix[i]+suffix[i]
            if s<minVal:
                minVal=s
                minIndex=i

        return minIndex