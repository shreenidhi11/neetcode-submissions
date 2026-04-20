# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # if not root:
        #     return ["N"]
        tree_string = []
        def helper(root):
            if not root:
                tree_string.append("N")
                return 
            tree_string.append(str(root.val))
            helper(root.left)
            helper(root.right)
        helper(root)
        return ",".join(tree_string)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree_data = data.split(",")
        self.index = 0

        def dfs():
            if tree_data[self.index] == "N":
                self.index += 1
                return None

            node = TreeNode(tree_data[self.index])
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


