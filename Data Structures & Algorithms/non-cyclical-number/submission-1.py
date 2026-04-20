class Solution:
    def isHappy(self, n: int) -> bool:
        numset = set()

        while n!=1:
            if n in numset:
                return False
            else:
                numset.add(n)
                n = self.returnSum(n)
        return True


    def returnSum(self,num):
        retsum = 0

        while num:
            # 19 -> 9
            digit = num % 10
            # 
            retsum = retsum + (digit ** 2)
            num = num // 10
        
        return retsum


        