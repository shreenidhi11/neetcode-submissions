# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = 0
        if not root:
            return max_path_sum

        # set for a single node
        max_path_sum = root.val
        
        def helper(root):
            nonlocal max_path_sum
            if not root:
                return 0
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            max_path_sum = max(max_path_sum, root.val + left + right)
            return root.val + max(left, right)
        
        helper(root)
        return max_path_sum
        


