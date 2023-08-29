from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.res=set()

        def recursion(i,j,eqn):
            if j>(len(num)+len(num)-1):
                if eval(eqn[:-1])==target:
                    self.res.add(eqn[:-1])
                return 

            if i<len(num):
                recursion(i+1,j+2,eqn+(str(num[i]+"+")))
                recursion(i+1,j+2,eqn+(str(num[i]+"-")))
                recursion(i+1,j+2,eqn+(str(num[i]+"*")))

        recursion(0,0,"")
        return list(self.res)
    
s=Solution()
print(s.addOperators("123",6))
# print(s.addOperators("123",6))

# print(s.addOperators("232",8))


# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:
#         dp={}
#         self.res=set()

#         def recursion(i,j,eqn):
#             if j>(len(num)+len(num)-1):
#                 # print(eqn,eqn[:-1], eval(eqn[:-1]))
#                 if eval(eqn[:-1])==target:
#                     self.res.add(eqn[:-1])
#                 return eval(eqn[:-1])==target

#             if (i, j, eqn) in dp:
#                 return dp[(i, j, eqn)]

#             ans=0

#             if i<len(num):
#                 ans+=recursion(i+1,j+2,eqn+(str(num[i]+"+")))
#                 ans+=recursion(i+1,j+2,eqn+(str(num[i]+"-")))
#                 ans+=recursion(i+1,j+2,eqn+(str(num[i]+"*")))
            
#             dp[(i, j, eqn)]=ans

#             return dp[(i, j, eqn)]

#         recursion(0,0,"")
#         return list(self.res)