# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def helper(root):
            nonlocal max_sum
            if not root:
                return 0
            left_sum = max(0, helper(root.left))
            right_sum = max(0, helper(root.right))
            max_sum = max(max_sum, left_sum + right_sum + root.val)
            return root.val + max(left_sum, right_sum)

        helper(root)
        return max_sum
        
        