"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_list = []
        q_list = []
        common_ancestor = None
        def findAncestorList(node, ancestors):
            if not node:
                return node
            ancestors.append(node)
            findAncestorList(node.parent, ancestors)

        findAncestorList(p, p_list)
        findAncestorList(q, q_list)

        i, j = len(p_list) - 1, len(q_list) - 1
        while i >= 0 and j >= 0:
            if p_list[i].val == q_list[j].val:
                common_ancestor = p_list[i]
            else:
                return common_ancestor
            i -= 1
            j -= 1

        return common_ancestor


