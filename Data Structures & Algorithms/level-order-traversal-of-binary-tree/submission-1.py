from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        res = []

        if not root:
            return []

        q.append(root)
        cnt = 1
        rescnt = 1

        while q:
            cnt = 0
            reslist =[]
            for i in range(rescnt):
                popp = q.popleft()
                reslist.append(popp.val)
                if popp.left:
                    q.append(popp.left)
                    cnt+=1
                if popp.right:
                    q.append(popp.right)
                    cnt+=1
            res.append(reslist)
            rescnt = cnt

        return res

                







        