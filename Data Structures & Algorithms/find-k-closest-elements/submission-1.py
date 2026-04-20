class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # first find all the difference sum
        mydict = defaultdict(list)
        ans = []

        for nums in arr:
            mydict[abs(x-nums)].append(nums)


        mydict = sorted(mydict.items())
        print(mydict)

        for index in range(len(mydict)):
            values = mydict[index][1]
            # print(values)
            for v in values:
                if k == 0:
                    break
                ans.append(v)
                k -= 1

        return sorted(ans)


