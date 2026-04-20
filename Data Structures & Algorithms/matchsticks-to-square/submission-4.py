class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        lenght = sum(matchsticks)
        sides = [0] * 4
        if lenght % 4 != 0:
            return False
        side_len = lenght // 4
        matchsticks.sort(reverse=True)
        def backtrack(index):
            if index == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[index] <= side_len:
                    sides[j] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[j] -= matchsticks[index]

                if sides[j] == 0:
                    break
            
            return False

        return backtrack(0)




        