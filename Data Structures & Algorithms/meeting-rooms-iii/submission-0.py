class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() #sort by start time

        count = [0 for i in range(n)] #count of rooms used
        used = [] #(end_time, room)
        available = [i for i in range(n)]

        for start, end in meetings:
            # removing all the meetings that are ended before a new meeting starts
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # case 1: there are no rooms available for this meetings
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            avail_room = heapq.heappop(available)
            heapq.heappush(used, (end, avail_room))

            count[avail_room] += 1

        return count.index(max(count))






















        