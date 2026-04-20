class Solution:
    def reverse(self, x: int) -> int:
        # define the MIN and Max
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x: 
            # modulo division %, this gives the remainder
            digit = int(math.fmod(x, 10))
            # gives the quotient
            x = int(x / 10)

            # greater than upper bound
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            # lesser than lower bound
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res


        