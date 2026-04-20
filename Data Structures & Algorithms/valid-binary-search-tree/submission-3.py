# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left, right = float("-inf"), float("inf")
        def check_valid(root, left, right):
            if not root:
                return True

            if not (left < root.val < right):
                return False

            return check_valid(root.left, left, root.val) and check_valid(root.right, root.val,right)

        return check_valid(root, left, right)
            
        
        