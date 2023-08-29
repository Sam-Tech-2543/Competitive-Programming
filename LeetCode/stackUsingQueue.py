# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque

class MyStack:

    def __init__(self):
        self.q=deque()
        self.c=0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.c+=1

    def pop(self) -> int:
        for i in range(self.c-1):
            n=self.q.popleft()
            self.q.append(n)
        
        n=self.q.popleft()
        self.c-=1
        return n

    def top(self) -> int:
        n=self.q[self.c-1]
        return n        

    def empty(self) -> bool:
        return self.c==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()