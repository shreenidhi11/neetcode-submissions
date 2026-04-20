class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)

        maxheap = [ -cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        q = deque()

        while maxheap or q:
            time+=1

            # process the elements in the maxheap
            if maxheap:
              idle_time =  1+ heapq.heappop(maxheap)
              # if idle_time is not zero only then add in the queue
              if idle_time:
                q.append([idle_time, time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time








        