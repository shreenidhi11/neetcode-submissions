class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # this is like Kadane Algorithm only, but we work on the difference 
        # between the gas we have and the cost to reach i+1 gas station


        if sum(gas) < sum(cost):
            return -1

        res = 0
        total = 0

        for i in range(len(gas)):
            total+= (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i+1

        return res
        