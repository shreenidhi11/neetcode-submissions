class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using quicksort algorithm to sort find the kth largest element
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
            









        