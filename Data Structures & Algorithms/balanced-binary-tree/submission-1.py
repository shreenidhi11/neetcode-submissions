# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            # nonlocal max_diameter
            if not root:
                return 0

            left = helper(root.left)
            if left == -1:
                return -1
            right = helper(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return  -1

            # max_diameter = max(max_diameter, left + right)

            return 1 + max(left, right)

        return False if helper(root) == -1 else True


        