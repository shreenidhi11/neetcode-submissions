class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # using quickselect algorithm - this algorithm's worst case tc is O(n ^ 2)
        #but this runs in linear time mostly. this is not a divide and conquer algo.
        # but very useful for finding the top or the smallest number
        #space complexity is O(1) and recursive call stack will be O(n) WC or O(logn)

        def quicksort(l, r):
            pivot = nums[r]
            p = l
            for index in range(l, r):
                if nums[index] <= pivot:
                    nums[index], nums[p] = nums[p], nums[index]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]
            return p
        
        l = 0
        r = len(nums) - 1
        k = len(nums) - k
        while True:
            partition_index = quicksort(l, r)
            if partition_index > k:
                r = partition_index - 1
            elif partition_index < k:
                l = partition_index + 1
            else:
                return nums[partition_index]



        