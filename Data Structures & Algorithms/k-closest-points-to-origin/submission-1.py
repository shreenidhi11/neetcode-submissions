class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_distance = []
        result = []
        for px, py in points:
            closest_distance.append((((px ** 2) + (py ** 2)),(px, py)))
        
        heapq.heapify(closest_distance)

        while k > 0:
           result.append(heapq.heappop(closest_distance)[1])
           k -= 1

        return result




        