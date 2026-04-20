from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in temperatures]

        s =  deque()

        s.append(0)

        j = 1

        while j < len(temperatures):
            while s and temperatures[s[-1]] < temperatures[j]:
                res[s[-1]] =  j  -  s[-1]
                s.pop()
            s.append(j)
            print(res)
            j+=1
        
        return res










        