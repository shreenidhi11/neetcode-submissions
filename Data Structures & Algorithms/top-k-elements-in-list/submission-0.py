class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # creating a count array
        count_arr = [[] for _ in range(len(nums) + 1)]

        mydict = {}
        ans = []

        for i in range(len(nums)):
            if nums[i] in mydict:
                mydict[nums[i]] = mydict[nums[i]] +1
            else:
                mydict[nums[i]] = 1

        for key, values in mydict.items():
            count_arr[values].append(key)

        cnt = 0
        while cnt != k:
            for i in reversed(range(len(count_arr))):
                if len(count_arr[i])!=0:
                    for j in count_arr[i]:
                        ans.append(j)
                        cnt+=1
                        if cnt == k:
                            return ans

        return ans




        






        