# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def helper(root, prev_max):
            nonlocal res
            if not root:
                return 0

            res = 1 if root.val >= prev_max else 0
            prev_max = max(root.val, prev_max)
            res += helper(root.left, prev_max)
            res += helper(root.right, prev_max)
            return res

        return helper(root, root.val)



        