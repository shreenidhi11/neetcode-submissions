# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            else:
                if p.val == q.val:
                    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
                else:
                    return False

        def helper(root, subRoot):
            if not root:
                return False

            if isSameTree(root, subRoot):
                return True

            return helper(root.left, subRoot) or helper(root.right, subRoot)

        return helper(root, subRoot)


            

            

        