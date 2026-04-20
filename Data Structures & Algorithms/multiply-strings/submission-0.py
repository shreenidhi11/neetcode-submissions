class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1)+len(num2))

        num1, num2 = num1[::-1], num2[::-1]
        digit = 0
        for n1 in range(len(num1)):
            for n2 in range(len(num2)):
                digit = int(num1[n1]) * int(num2[n2])
                # add the multiply result in n1+n2, but if there
                # is already something then add that as well
                res[n1+n2] += digit
                # adding the carry bit now
                res[n1+n2+1]+= res[n1 + n2] // 10
                res[n1+n2] = res[n1+n2] % 10

        res,beg = res[::-1], 0
        # avoid all the zeroes
        while beg < len(res) and res[beg] == 0:
            beg+=1

        # convert into string
        res = map(str, res[beg:])
        return "".join(res)




        