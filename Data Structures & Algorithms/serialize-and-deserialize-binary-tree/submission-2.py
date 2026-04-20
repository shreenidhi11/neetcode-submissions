# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes_list = []
        def helper(root):
            if not root:
                nodes_list.append("N")
                return
            nodes_list.append(str(root.val))
            helper(root.left)
            helper(root.right)

        helper(root)
        return ",".join(nodes_list)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree_nodes = data.split(",")
        self.index = 0
        def dfs():
            if tree_nodes[self.index] == "N":
                self.index += 1
                return
            new_node = TreeNode(tree_nodes[self.index])
            self.index += 1
            new_node.left = dfs()
            new_node.right = dfs()
            return new_node
        return dfs()

