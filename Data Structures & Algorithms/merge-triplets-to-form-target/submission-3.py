class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res_set = set()
        for index in range(len(triplets)):
            if triplets[index][0] > target[0] or triplets[index][1] > target[1] or triplets[index][2] > target[2]:
                continue
            
            for i, value in enumerate(triplets[index]):
                if value == target[i]:
                    res_set.add(i)

        return len(res_set) == 3






        