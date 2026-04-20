class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # reassign the value of k with the exact index of the kth largest element
        k = len(nums) - k
        def quickselect(l,r):
            p, pivot = l, nums[r]
            for i in range(l,r):
                if nums[i] <= pivot:
                    # swap this 
                    nums[p], nums[i] = nums[i], nums[p]
                    p +=1
            nums[r], nums[p] = nums[p],nums[r]

            if p > k: return quickselect(l,p-1)
            elif p < k : return quickselect(p+1,r)
            else:
                return nums[p]

        return quickselect(0,len(nums)-1)



            






        


        