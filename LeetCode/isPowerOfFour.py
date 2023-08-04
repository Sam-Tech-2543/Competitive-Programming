class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # while n>1:
        #     n=n/4
        # return n==1

        # t=int('101010101010101010101010101010',2)
        # if n!=0 and n&(n-1)==0 and n&t==0:
        #     return True
        # return False

        return (
            n > 0
            and n & (n - 1) == 0
            and n & int("101010101010101010101010101010", 2) == 0
        )