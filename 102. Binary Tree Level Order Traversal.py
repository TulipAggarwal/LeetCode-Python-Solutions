# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root] if root else [])
        ans = []
        while len(queue):
            qlen = len(queue)
            row = []
            for _ in range(qlen):
                curr = queue.popleft()
                row.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
            ans.append(row)
        return ans
