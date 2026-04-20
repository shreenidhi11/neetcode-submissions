# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            else:
                return helper(p.right, q.right) and helper(p.left, q.left)


        def isSub(root, subRoot):
            if not subRoot:
                return True

            if not root:
                return False

            if helper(root, subRoot):
                return True

            else:
                return isSub(root.left, subRoot) or isSub(root.right, subRoot)

        
        return isSub(root, subRoot)

            




        


            

        