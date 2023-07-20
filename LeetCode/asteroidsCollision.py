# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()
                if stack and stack[-1]==abs(asteroids[i]):
                    stack.pop()
                elif not stack or stack[-1]<0:
                    stack.append(asteroids[i])

        return stack

s=Solution()

# asteroids=[5,10,-5]
# print(s.asteroidCollision(asteroids))

# asteroids=[8,-8]
# print(s.asteroidCollision(asteroids))

# asteroids=[10,2,-5]
# print(s.asteroidCollision(asteroids))

asteroids=[-2,-1,1,2]
print(s.asteroidCollision(asteroids))

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack=[asteroids[0]]

#         for i in range(1,len(asteroids)):
#             while stack and (asteroids[i]<0<stack[-1] or stack[-1]<0<asteroids[i]):
#                 if abs(asteroids[i])>abs(stack[-1]):
#                     stack.pop()
#                 elif abs(asteroids[i])<abs(stack[-1]):
#                     break
#                 elif abs(asteroids[i])==abs(stack[-1]):
#                     stack.pop()
#                     break
#                 else:
#                     break
#             else:
#                 stack.append(asteroids[i])

#         return stack