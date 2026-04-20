class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # do it again
        minheap = []
        count = Counter(hand)

        minheap = list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]

            for index in range(first, first + groupSize):
                if index not in count:
                    return False
                count[index] -= 1

                if count[index] == 0:
                    if index != minheap[0]:
                        return False
                    heapq.heappop(minheap)

        return True








        