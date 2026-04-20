# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_value = root.val
        while root:
            if abs(target - root.val) < abs(closest_value - target):
                closest_value = root.val

            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            elif root.val == target:
                return root.val

        return closest_value

    # tc is O(H)
    #  sc is O(1)



        