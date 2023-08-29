class Solution:
    def climbStairs(self, n: int) -> int:

        # lst=[i for i in range(n-1)]
        # lst.append(1)
        # lst.append(1)

        # for i in range(len(lst)-3,-1,-1):
        #     lst[i]=lst[i+1]+lst[i+2]

        # return lst[0]

        # secondLast,last=1,1

        # for i in range(0,n-1):
        #     temp=secondLast
        #     secondLast=last+temp
        #     last=temp

        # return secondLast
        
        dp={}

        def recursion(curr):
            if curr in dp:
                return dp[curr]
            if curr==1:
                return 1
            if curr==2:
                return 2

            dp[curr]=recursion(curr-2)+recursion(curr-1)
            return dp[curr]

        return recursion(n)
    

s=Solution()
print(s.climbStairs(5))