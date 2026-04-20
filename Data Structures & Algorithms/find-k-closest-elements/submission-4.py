class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # first find all the difference sum
        # mydict = defaultdict(list)
        # ans = []

        # for nums in arr:
        #     mydict[abs(x-nums)].append(nums)


        # mydict = sorted(mydict.items())
        # print(mydict)

        # for index in range(len(mydict)):
        #     values = mydict[index][1]
        #     # print(values)
        #     for v in values:
        #         if k == 0:
        #             break
        #         ans.append(v)
        #         k -= 1

        # return sorted(ans)
# another solution
# first find the element x or the element that is greater than x using binary search and then use 2 points to increase the range
        l, r = 0 , len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid

        # now increase the window
        l , r = l - 1, l
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1

        return arr[l + 1:r] 




