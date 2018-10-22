#Method 1: Recursively

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        stack=[]
        self.dfs(root,stack)
        return stack
    
    def dfs(self,root,stack):
        curr = root
        if curr.left:
            self.dfs(curr.left,stack)
        if curr.right:
            self.dfs(curr.right,stack)
        stack.append(curr.val)
