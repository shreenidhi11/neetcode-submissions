class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # checking if we can make hands of given groupsize from the given length
        if len(hand) % groupSize != 0:
            return False

        # keep count of all the values in hand
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)

        # now get all the keys in the minheap
        minheap = list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]

            for nums in range(first, first+groupSize):
                # check if this number is there in count dict
                if nums not in count:
                    return False
                count[nums] -=1
                
                if count[nums] == 0:

                    if nums != minheap[0]:
                        return False
                    heapq.heappop(minheap)

        return True

                




        

        