# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        tmp = root

        while tmp:
            if p.val < tmp.val and q.val < tmp.val:
                tmp = tmp.left
            elif p.val > tmp.val and q.val > tmp.val:
                tmp = tmp.right
            else:
                return tmp

        # tc and sc will be O(h)
        
        