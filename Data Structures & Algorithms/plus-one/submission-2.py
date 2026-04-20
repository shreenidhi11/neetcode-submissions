class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            stres =  str(digits[0]+1)
            if len(stres) > 1:
                return [stres[0], stres[1] ]
            else:
                return [stres[0]]

        res = 10 * digits[0]

        for i in range(1,len(digits)):
            res = res + digits[i]
            if i == len(digits)-1:
                break
            res*=10

        print(res)
        res = res + 1

        reslist = []

        for ch in str(res):
            reslist.append(ch)

        return reslist

            

        