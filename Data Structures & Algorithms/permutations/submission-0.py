class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # [1,2,3]
        res = []

        # base case:
        if len(nums) == 1:
            return [nums[:]]


        for i in range(len(nums)):
            n = nums.pop(0) #removed the first element [2,3], 
            # find permutations for 2 and 3 now
            perms = self.permute(nums)

            # now add 1 in all the permutations
            for perm in perms:
                perm.append(n)
            
            # add the final list of permutstions
            res.extend(perms)
            nums.append(n)
        
        return res








        