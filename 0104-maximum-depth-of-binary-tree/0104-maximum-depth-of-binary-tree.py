# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root,1)])
        res = 0

        while queue:
            tot = len(queue)
            for _ in range(len(queue)):
                node,depth = queue.popleft()
                res = max(res,depth)
                if node.left:
                    queue.append((node.left,depth+1))
                if node.right:
                    queue.append((node.right,depth+1))
        return res 