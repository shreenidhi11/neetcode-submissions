# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, max_value):
            if not root:
                return 0
            count = 1 if root.val >= max_value else 0
            max_value = max(max_value, root.val)
            count += helper(root.left, max_value)
            count += helper(root.right, max_value)
            return count

        return helper(root, root.val)


        