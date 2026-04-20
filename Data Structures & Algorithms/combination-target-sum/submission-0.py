class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res= []

        curr = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= len(nums):
                return 

            curr.append(nums[i])
            # when you include the same element more than once
            dfs(i, curr, total + nums[i])

            curr.pop()
            # when you dont want to include the same element
            dfs(i+1, curr, total)


        dfs(0,[],0)

        return res





            


        