class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # check if either of the number is zero
        if "0" in [num1,num2]:
            return "0"

        # reverse the numbers
        num1, num2 = num1[::-1], num2[::-1]

        # define the res list to store the result
        res= [0] * (len(num1)+ len(num2))

        # start multiplying
        for n1 in range(len(num1)):
            for n2 in range(len(num2)):
                res[n1+n2] += int(num1[n1]) * int(num2[n2])
                # adding the carry digit to the next location
                res[n1+n2+1]+= res[n1+n2] // 10
                res[n1+n2] = res[n1+n2] % 10

        # now you need to format the result
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg +=1

        res = map(str, res[beg:])

        return "".join(res)

        









        