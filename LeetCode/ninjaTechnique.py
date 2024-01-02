from typing import *

# class solution:
#     def recursion(self,curr, last, tot):
#         if curr==self.n:
#             self.res=max(self.res,tot)
#             return

#         for i in range(3):
#             if i!=last:
#                 # if self.dp[curr][i]!=-1:
#                 #     ans=self.dp[curr][i]
#                 # else:
#                 #     ans=self.recursion(curr+1,i,tot+self.points[curr][i])
#                 #     self.dp[curr][i]=ans
#                 ans=self.recursion(curr+1,i,tot+self.points[curr][i])
#                 self.dp[curr][i]=ans


#     def ninjaTraining(self, n: int, points: List[List[int]]) -> int:
#         # Write your code here.
#         self.dp=[[-1,-1,-1] for i in range(n)]
#         self.points=points
#         self.n=n
#         self.res=float('-inf')

#         self.recursion(0,3,0)

#         return self.res
    
# s=solution()

# # 3
# # 1 2 5 
# # 3 1 1
# # 3 3 3
# print(s.ninjaTraining(3,[[1,2,5],[3,1,1],[3,3,3]]))

# # 3
# # 10 40 70
# # 20 50 80
# # 30 60 90
# print(s.ninjaTraining(3,[[10,40,70],[20,50,80],[30,60,90]]))


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    # Write your code here.
    dp=[0,0,0]
    for i in range(n):
        n1=points[i][0]+max(dp[1],dp[2])
        n2=points[i][1]+max(dp[0],dp[2])
        n3=points[i][2]+max(dp[0],dp[1])

        dp=[n1,n2,n3]

    return max(dp)


# 3
# 1 2 5 
# 3 1 1
# 3 3 3
print(ninjaTraining(3,[[1,2,5],[3,1,1],[3,3,3]]))

# 3
# 10 40 70
# 20 50 80
# 30 60 90
print(ninjaTraining(3,[[10,40,70],[20,50,80],[30,60,90]]))
