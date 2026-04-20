from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:    
            return None

        q = deque()

        q.append(root)

        while q:
            popp = q.popleft()
            tmp = popp.left
            popp.left = popp.right
            popp.right = tmp

            if popp.left:
                q.append(popp.left)
            if popp.right:
                q.append(popp.right)
        
        return root




        
        











                



            
        