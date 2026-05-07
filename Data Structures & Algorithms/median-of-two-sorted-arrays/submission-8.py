class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # work on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        total_length = n1 + n2
        half_length = (total_length + 1) // 2 #handle even and odd length
        l, r = 0, n1
        while l <= r:
            mid1 = (l + r) // 2
            mid2 = half_length - mid1
            l1, l2, r1, r2  = float("-inf"), float("-inf"), float("inf"), float("inf")
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            # correct condition
            if l1 <= r2 and l2 <= r1:
                if total_length % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            # incorrect partition 
            if l2 > r1:
                l = mid1 + 1
            else:
                r = mid1 - 1

