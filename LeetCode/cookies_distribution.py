# 2305. Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution(object):
    minVal=float('inf')
    k,l=0,0

    def solution_using_backtracking(self, cookies, i, bags):
        if(i==self.l):
            self.minVal=min(self.minVal,max(bags))
            return

        for j in range(self.k):
            bags[j]+=cookies[i]
            if(bags[j]>self.minVal):
                bags[j]-=cookies[i]
                continue
            self.solution_using_backtracking(cookies, i+1, bags)
            bags[j]-=cookies[i]

    def distributeCookies(self, cookies, k):
        self.k=k
        self.l=len(cookies)
        self.solution_using_backtracking(cookies, 0, [0] * k)
        return self.minVal



s=Solution()
print(s.distributeCookies([8,15,10,20,8], 2))
print(s.distributeCookies([6,1,3,2,2,4,1,2], 3))


class Solution(object):
    def __init__(self):
        self.result = float('inf')

    def distributeCookies(self, cookies, k):
        N = len(cookies)
        L = [0] * k

        def dfs(i, val):
            if val >= self.result:
                return
            if i == N:
                self.result = min(self.result, val)
                return
            for j in range(k):
                L[j] += cookies[i]
                dfs(i + 1, max(val, L[j]))
                L[j] -= cookies[i]

        dfs(0, 0)
        return self.result	
