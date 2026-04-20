class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(curr_weight):
            sum_ = 0
            day = 0
            for w in weights:
                sum_ += w
                if sum_ > curr_weight:
                    day += 1
                    sum_ = 0
                    sum_ += w
                
            return True if day < days else False

        l, r = max(weights), sum(weights)
        result = 0
        while l <= r:
            current_max_weight = (l + r) // 2
            if canShip(current_max_weight):
                r = current_max_weight - 1
                result = current_max_weight
            else:
                l = current_max_weight + 1

        return result




        

