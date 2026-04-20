# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #using postorder approach (left right root)
        def helper(root):
            if not root:
                return None

            root.left, root.right = helper(root.left), helper(root.right)
            if not root.left and not root.right and root.val == target:
                return None
            else:
                return root

        return helper(root)

        #tc is O(n)
        #sc is height of the binary tree 