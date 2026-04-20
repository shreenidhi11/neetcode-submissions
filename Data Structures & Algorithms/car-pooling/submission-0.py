class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # The heap maintains (end of trip, #passengers)
        trips.sort(key=lambda x: x[1])
        current_pasengers = 0
        minheap = []
        for seats, pick, end in trips:
            # remove all the passengers from the previous trip when a drop off location is reached
            while minheap and minheap[0][0] <= pick:
                   prev_end, passengers = heapq.heappop(minheap)
                   current_pasengers -= passengers

            # if the current_passengers exceed capacity then break
            current_pasengers += seats
            if current_pasengers > capacity:
                return False

            heapq.heappush(minheap, [end, seats])
        return True

        # tc is nlogn
        # sc is o(n)

        