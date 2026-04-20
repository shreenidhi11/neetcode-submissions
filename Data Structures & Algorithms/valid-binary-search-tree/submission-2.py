# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left, right = float("-inf"), float("inf")
        def helper(left, root, right):
            if not root:
                return True

            if not (left < root.val < right):
                return False

            return helper(left, root.left, root.val) and helper(root.val, root.right, right)

        return helper(left, root, right)
