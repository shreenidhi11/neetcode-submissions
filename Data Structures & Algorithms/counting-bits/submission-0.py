class Solution:
    def countBits(self, n: int) -> List[int]:
        oneslist = []
        onescnt = 0

        def calculate(number):
            res = 0
            while number:
                number&=(number-1)
                res+=1
            return res

        for i in range(n+1):
            if i == 0:
                oneslist.append(0)
            elif i == 1:
                oneslist.append(1)
            else:
                oneslist.append(calculate(i))

        return oneslist







        