# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {value:index for index, value in enumerate(inorder)}
        self.index = 0

        def helper(l, r):
            if l > r:
                return None

            root = TreeNode(preorder[self.index])
            partition = index_map[preorder[self.index]]
            self.index += 1
            root.left = helper(l, partition - 1)
            root.right = helper(partition + 1, r)
            return root

        return helper(0, len(inorder) - 1)









    #TC is o(n2), due to using the find index method 
        

