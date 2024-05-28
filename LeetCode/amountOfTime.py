from typing import Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = list()

    def inorder(self, root: Optional[TreeNode]):
        if root:
            self.inorder(root.left)
            self.nodes.append(root.val)

            if root.left:
                self.graph[root.val].append(root.left.val)
                self.graph[root.left.val].append(root.val)
            if root.right:
                self.graph[root.val].append(root.right.val)
                self.graph[root.right.val].append(root.val)
            self.inorder(root.right)


    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.inorder(root)
        print(self.graph)

        ans=-1
        q=deque([start])
        visited=set()
        visited.add(start)

        while q:
            size=len(q)
            for _ in range(size):
                node=q.popleft()
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            ans+=1

        return ans
    
s=Solution()

# Input: root = [1,5,3,null,4,10,6,9,2], start = 3

root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)

print(s.amountOfTime(root, 3))



# class Solution:
#     def __init__(self):
#         self.graph = defaultdict(list)
#         self.nodes = list()

#     def inorder(self, root: Optional[TreeNode]):
#         if root:
#             self.inorder(root.left)
#             self.nodes.append(root.val)

#             if root.left:
#                 self.graph[root.val].append(root.left.val)
#                 self.graph[root.left.val].append(root.val)
#             if root.right:
#                 self.graph[root.val].append(root.right.val)
#                 self.graph[root.right.val].append(root.val)
#             self.inorder(root.right)


#     def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
#         self.inorder(root)
#         print(self.graph)

#         ans=0
#         c=1
#         started=[start]
#         affected=[start]
#         targetNodes=len(self.nodes)
        
#         while c!=targetNodes:
#             temp=[]
#             for i in started:
#                 for j in self.graph[i]:
#                     if j not in affected:
#                         temp.append(j)
#                         affected.append(j)
#                         c+=1
#             started=temp
        
#             print(f"{started=}")
#             ans+=1

#         return ans