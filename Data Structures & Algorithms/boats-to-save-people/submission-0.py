class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort to pair light and heavy weight people together
        total_boats = 0
        people.sort()
        l, r = 0, len(people) - 1

        while l <= r:
            total_boats += 1
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1


        return total_boats 
            






        