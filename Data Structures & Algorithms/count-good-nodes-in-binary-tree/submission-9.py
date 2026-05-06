# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, prev_max):
            if not node:
                return 0
            count = 1 if node.val >= prev_max else 0
            prev_max = max(prev_max, node.val)
            count += helper(node.left, prev_max)
            count += helper(node.right, prev_max)
            return count
        
        return helper(root, root.val)


        