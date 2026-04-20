class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            n1, n2 = n2, n1
            nums1, nums2 = nums2, nums1

        total_length = n1 + n2
        correct_left_half = ((total_length + 1 )// 2)
        l, r = 0, n1
        while l <= r:
            mid1 = (l + r) // 2
            mid2 = correct_left_half - mid1
            l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            #checking the valid conidtion
            if l1 <= r2 and l2 <= r1:
                if total_length % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0

            if l2 > r1:
                l = mid1 + 1
            else:
                r = mid1 - 1

    

