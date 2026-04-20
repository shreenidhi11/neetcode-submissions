# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        value_map = defaultdict(list)
        if not root:
            return []

        q.append([0, root])
        while q:
            val, node = q.popleft()
            value_map[val].append(node.val)
            if node.left:
                q.append([val - 1, node.left])
            if node.right:
                q.append([val + 1, node.right])
        result = []
        sorted_by_key = dict(sorted(value_map.items()))
        for keys in sorted_by_key:
            result.append(sorted_by_key[keys])

        return result
 



        