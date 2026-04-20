class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        totalUsed = 0
        start = 0
        for index in range(len(gas)):
            totalUsed += (gas[index] -  cost[index])
            if totalUsed < 0:
                totalUsed = 0
                start = index + 1
        
        return start




        

        
        