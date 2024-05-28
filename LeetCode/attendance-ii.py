# class Solution:
#     def checkRecord(self, n: int) -> int:
#         s=['A','L','P']
#         ans=0

#         def dfs(i, curr):
#             nonlocal ans

#             if curr.count("A")>=2 or 'LLL' in curr:
#                 return
#             else:
#                 if i==n:
#                     # print(curr)
#                     ans+=1
#                     return
            
#             for j in s:
#                 curr+=j
#                 i+=1
#                 dfs(i, curr)
#                 i-=1
#                 curr=curr[:-1]

#         dfs(0, "")
#         return ans
                        
# s=Solution()
# # print(s.checkRecord(2))
# print(s.checkRecord(100))

from collections import defaultdict

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD=10**9 + 7
        cache={}
        def dfs(i):
            if i==1:
                return {
                    (0,0): 1, (0,1): 1, (0,2):0,
                    (1,0): 1, (1,1): 0, (1,2):0 
                }

            if n in cache:
                return cache[n]

            temp=dfs(i-1)
            res=defaultdict(int)

            # Choose P    
            res[(0,0)]=((temp[(0,0)]+temp[0,1]) % MOD + temp[(0,2)])%MOD
            res[(1,0)]=((temp[(1,0)]+temp[1,1]) % MOD + temp[(1,2)])%MOD

            # Choose L
            res[(0,1)] = temp[0,0]
            res[(1,1)] = temp[1,0]
            res[(0,2)] = temp[0,1]
            res[(1,2)] = temp[1,1]

            # Choose A
            res[(1,0)] = (res[(1,0)] + ((temp[(0,0)]+temp[(0,1)])%MOD + temp[(0,2)]) %MOD) % MOD
            cache[n]=res
            
            return res
        
        return sum(dfs(n).values()) % MOD
