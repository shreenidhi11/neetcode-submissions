class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_len = n1 + n2
        correct_left = (n1 + n2 + 1) // 2

        l, r = 0, n1
        while l <= r:
            # find the total no. of elements from n1
            mid1 = (l + r) // 2
            # find the rest from n2
            mid2 = correct_left - mid1
            l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if total_len % 2 == 1:
                    return max(l1, l2)
                else:
                    # return (float(max(l1, l2)) + float(min(r1, r2)) / 2.0)
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1