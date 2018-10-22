#Method 1: Recursively

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        stack = []
        self.dfs(root, stack)
        return stack
    
    
    def dfs(self, root, stack):
        cur = root
        stack.append(cur.val)
        if cur.left:
            self.dfs(root.left, stack)
        if cur.right:
            self.dfs(root.right, stack)
