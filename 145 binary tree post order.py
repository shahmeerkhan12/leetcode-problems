# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res = []

        def post_traversal(node):

            if not node:
                return
            
            post_traversal(node.left)
            post_traversal(node.right)
            res.append(node.val)

        post_traversal(root)

        return res
        
