"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

#using the recursive approach:
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        def dfs (node): #using a depth first search 
            if not node: 
                return
            output.append(node.val)
            for c in node.children:
                dfs(c) #recursing the function
        dfs(root)
        return(output)
